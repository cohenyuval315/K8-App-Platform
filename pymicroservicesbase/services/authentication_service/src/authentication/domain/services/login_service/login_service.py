import re
from urllib.parse import urlencode

from fastapi import Response
from pydantic import AliasChoices, Field, ValidationError

from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.authentication_service.logger import logger

# from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.authentication_responses import AuthenticationResponseModel

# from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.account_recovery_responses import AccountRecoveryResponseModel
# from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.account_recovery.account_recovery_command import AccountRecoveryCommand
# from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.authentication_command.authentication_command import AuthenticationCommand
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)

from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.session_key_manager import (
    SessionKeyManager,
)

from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session import (
    UserSessionData,
)

from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads import (
    LoginPayload,  # type: ignore
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads import (
    SessionPayload,  # type: ignore
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads import (
    AccessPayload,
    AccessTokenPayload,
    ProductPayload,
    RefreshTokenPayload,
    SessionTokenPayload,
    UserPayload,
)

from pymicroservicesbase.utils.security.password import (
    verify_password,
)
from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_string,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType


from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pydantic import EmailStr
from pymicroservicesbase.sdk.web_api.common.types.username_type import (
    UserNameStrType,
)
from pymicroservicesbase.sdk.web_api.common.types.password_type import (
    PassWordStrType,
)
from pymicroservicesbase.shared.constants.media_type import MediaType


class LoginPasswordBody(BaseModel):
    identifier: EmailStr | UserNameStrType = Field(
        validation_alias=AliasChoices("email", "username", "identifier")
    )
    password: PassWordStrType


class LoginService:
    def __init__(
        self,
        user_service,
        token_service,
        user_active_session_service,
        cookies_manager,
        internal_service_access,
        refresh_token_expire,
        access_token_expire,
        session_token_expire,
        session_id_token_expire,
        csrf_token_expire,
        session_ttl,
        with_active_session: bool,
    ):
        self.session_key_manager = SessionKeyManager()
        self.internal_service_access = internal_service_access
        self.user_service = user_service
        self.token_service = token_service
        self.user_active_session_service = user_active_session_service
        self.cookies_manager = cookies_manager
        self.login_method_handlers = {
            "password": self.login_password,
            # "oauth":None,
            # "totp": None
        }
        self.refresh_token_expire = refresh_token_expire
        self.access_token_expire = access_token_expire
        self.session_token_expire = session_token_expire
        self.session_id_token_expire = session_id_token_expire
        self.csrf_token_expire = csrf_token_expire
        self.session_ttl = session_ttl

    async def _login_password(self, command: LoginCommand) -> UserPayload:
        logger.info(
            "Processing login with password for login method: %s",
            command.login_method,
        )
        body = await command.request.json()
        try:
            creds = LoginPasswordBody.model_validate(body)
            logger.debug("Login body validated successfully")
        except ValidationError:
            logger.error("Validation error for login body", exc_info=True)
            raise WebServiceError(
                error_message=f"invalid request body for login method {command.login_method}",
                error_code=400,
            )

        field = None
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        username_pattern = r"^[\w]+$"

        if re.match(email_pattern, creds.identifier):
            field = "email"
        elif re.match(username_pattern, creds.identifier):
            field = "username"

        if field is None:
            logger.warning("Invalid identifier: %s", creds.identifier)
            raise WebServiceError(
                error_message=f"invalid identifer for login method {command.login_method}",
                error_code=400,
            )

        response = await self.user_service.get_users(
            filters=[
                {"field": field, "value": creds.identifier, "operator": "eq"}
            ],
        )
        logger.debug("User service response: %s", response)

        if not response.is_success:
            logger.error("User service response was not successful")
            raise WebServiceError(
                error_message="user service response was not successful, 'get' should always be successful in get many users context",
                error_code=500,
                errors=[WebServiceError.unpack(response)],
            )

        try:
            res = response.json()
            data = res["data"]
            if len(data) != 1:
                logger.warning(
                    "User not found for %s: %s", field, creds.identifier
                )
                raise WebServiceError(
                    error_message=f"{field} '{creds.identifier}' does not exists",
                    is_public=True,
                    error_code=401,
                )
            user = data[0]
            hashed_password = user["hashed_password"]
        except (KeyError, IndexError):
            logger.error("Failed to parse user response", exc_info=True)
            raise WebServiceError(
                title="failed to parse user repsonse",
                description="failed to parse user repsonse",
                error_code=500,
            )

        is_success = verify_password(creds.password, hashed_password)
        if not is_success:
            logger.warning("Invalid password for user: %s", creds.identifier)
            raise WebServiceError(
                error_message="Invalid password",
                error_code=401,
                is_public=True,
            )
        try:
            user_payload = UserPayload.model_validate(user)
            logger.info("User payload validated successfully")
            return user_payload
        except ValidationError:
            logger.error("Failed to parse user payload", exc_info=True)
            raise WebServiceError(
                title="user payload failed to parse user", error_code=500
            )

    async def login_password(self, command: LoginCommand):
        logger.info(
            "Handling password login for product: %s", command.product_id
        )
        user_payload = await self._login_password(command)
        logger.debug("User payload: %s", user_payload)

        session_id_token = await self.token_service.generate_session_id_token()

        logger.debug("Generated tokens: session_id_token=%s", session_id_token)

        user_session_data = UserSessionData(
            last_activity=datetime_to_string(utcnow()),
            user_id=user_payload.user_id,
            product_id=command.product_id,
            extend_count=0,
            session_id=session_id_token,
            user_email=user_payload.user_email,
            user_username=user_payload.user_username,
        ).model_dump()

        logger.debug(
            "User Active Session Data to be created: %s", user_session_data
        )

        session_response = await self.user_active_session_service.create_user_session(
            session_key=session_id_token,
            user_set_key=self.session_key_manager.get_user_sessions_key(
                user_payload.user_id
            ),
            value=user_session_data,
            expire_at=self.session_ttl,
            product_set_key=self.session_key_manager.get_product_sessions_key(
                command.product_id
            ),
        )

        logger.debug(
            "User Active Session Creation Response: %s", session_response
        )

        session_payload = SessionPayload(session_id=session_id_token)
        product_payload = ProductPayload(product_id=command.product_id)
        access_payload = AccessPayload.model_validate(
            self.internal_service_access
        )
        login_payload = LoginPayload(
            login_method="password",
            login_provider=None,
        )

        csrf_token = await self.token_service.generate_csrf_token()
        session_token = await self.token_service.generate_session_token(
            SessionTokenPayload(
                product=product_payload,
                session=session_payload,
                user=user_payload,
            ),
            self.session_token_expire,
        )
        access_token = await self.token_service.generate_access_token(
            AccessTokenPayload(
                access=access_payload,
                product=product_payload,
                user=user_payload,
            ),
            self.access_token_expire,
        )

        refresh_token = await self.token_service.generate_refresh_token(
            RefreshTokenPayload(
                product=product_payload, user=user_payload, login=login_payload
            ),
            self.refresh_token_expire,
        )

        self.cookies_manager.set_cookie(
            command.response,
            TokenKeyType.ACCESS_TOKEN.value,
            access_token,
            self.access_token_expire,
        )

        self.cookies_manager.set_cookie(
            command.response,
            TokenKeyType.REFRESH_TOKEN.value,
            refresh_token,
            self.refresh_token_expire,
        )

        self.cookies_manager.set_cookie(
            command.response,
            TokenKeyType.SESSION_ID_TOKEN.value,
            session_id_token,
            self.session_id_token_expire,
        )

        self.cookies_manager.set_cookie(
            command.response,
            TokenKeyType.SESSION_TOKEN.value,
            session_token,
            self.session_token_expire,
        )

        self.cookies_manager.set_cookie(
            command.response,
            TokenKeyType.CSRF_TOKEN.value,
            csrf_token,
            self.csrf_token_expire,
        )

        tokens_data = {
            "access_token": {
                "token_value": access_token,
                "token_expire": self.access_token_expire,
                "token_type": "Bearer",
            },
            "refresh_token": {
                "token_value": refresh_token,
                "token_expire": self.refresh_token_expire,
                "token_type": "Bearer",
            },
            "session_token": {
                "token_value": session_token,
                "token_expire": self.session_token_expire,
                "token_type": "Bearer",
            },
            "session_id_token": {
                "token_value": session_id_token,
                "token_expire": self.session_id_token_expire,
                "token_type": "uuid",
            },
            "csrf_token": {
                "token_value": csrf_token,
                "token_expire": self.csrf_token_expire,
                "token_type": "uuid",
            },
        }

        logger.debug(tokens_data)
        urlencoded_content = urlencode({"session_id": session_id_token})
        _response = Response(
            content=urlencoded_content,
            media_type=MediaType.FORM_URLENCODED,
            headers=command.response.headers,
            status_code=200,
        )
        return _response

    async def login(self, command: LoginCommand) -> Response:
        logger.info("Processing login with method: %s", command.login_method)
        try:
            handler = self.login_method_handlers[command.login_method]
            response = await handler(command=command)
            return response
        except KeyError:
            logger.error(
                "Invalid login method: %s", command.login_method, exc_info=True
            )
            raise WebServiceError(
                error_message=f"invalid login method = {command.login_method}",
                error_code=400,
            )
