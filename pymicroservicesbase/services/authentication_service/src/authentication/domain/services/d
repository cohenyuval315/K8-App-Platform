import re

from cryptography.fernet import Fernet
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from pymicroservicesbase.sdk.services.internal.internal_user_service_client import (
    InternalUserServiceClient,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.authentication_service.logger import logger

# from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.authentication_responses import AuthenticationResponseModel
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_product_authentication_data_command import (
    GetProductAuthenticationDataCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_user_authentication_data_command import (
    GetUserAuthenticationDataCommand,
)

# from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.account_recovery_responses import AccountRecoveryResponseModel
# from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.account_recovery.account_recovery_command import AccountRecoveryCommand
# from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.authentication_command.authentication_command import AuthenticationCommand
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.logout.logout_command import (
    LogoutCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.refresh.refresh_command import (
    RefreshCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.register.register_command import (
    RegisterCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.verify_command import (
    VerifyCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.whoami_command import (
    WhoAmICommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.login_responses import (
    LoginResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.logout_responses import (
    LogoutResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.register_responses import (
    RegisterResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.providers.auth_provider_service import (
    AuthProviderService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_active_session_service import (
    UserActiveSessionService,  # type: ignore
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session import (
    UserSessionData,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session_service import (
    UserSessionService,
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
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.tokens_service import (
    TokenService,
)
from pymicroservicesbase.services.authentication_service.src.cookies.cookies_manager import (
    CookiesManager,
)

from pymicroservicesbase.utils.security.password import (
    verify_password,
)
from pymicroservicesbase.shared.constants.headers import (
    CSRF_TOKEN_HEADER_KEY,
)
from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_string,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType

# from packages.python.project_core.project_web_api.src.web_api.dependancies.product import ProductRegister
# from packages.python.project_core.project_web_api.src.web_api.dependancies.service import ServiceRegister
# from services.user_microservice.user_microservice.users.utils.security import

# LoginMethodType,
# MobileLoginMethod,
# TokenLoginMethod,
# OAuthLoginMethod


class AuthenticationService:
    def __init__(
        self,
        user_service: InternalUserServiceClient,
        user_session_service: UserSessionService,
        user_active_session_service: UserActiveSessionService,
        cookies_manager: CookiesManager,
        token_service: TokenService,
        auth_provider_service: AuthProviderService,
    ):
        self.user_service = user_service
        self.session_service = user_session_service
        self.cookies_manager = cookies_manager
        self.auth_provider_service = auth_provider_service
        self.token_service = token_service
        self.user_active_session_service = user_active_session_service
        self.internal_service_access = {
            "client_id": "auth_client_id",
            "client_secret": "auth_client_id",
            "scope": "",
        }
        self.FERNET_SECRET_KEY = Fernet.generate_key()
        self.cipher_suite = Fernet(self.FERNET_SECRET_KEY)

        self.refresh_token_expire = 24 * 60 * 60
        self.access_token_expire = 20 * 60
        self.session_token_expire = 10 * 60

        self.session_id_token_expire = 5 * 60
        self.csrf_token_expire = 5 * 60
        self.session_ttl = 5 * 60

    def get_user_sessions_key(self, user_id: str) -> str:
        return f"{user_id}:sessions"

    def get_product_sessions_key(self, product_id: str) -> str:
        return f"{product_id}:sessions"

    async def register_user(
        self, command: RegisterCommand
    ) -> RegisterResponseModel:
        params = {
            "view_type": "admin",
        }
        if len(command.username) == 0:
            command.username = command.email
        register_data = command.model_dump(
            exclude=["response", "request", "register_method"]
        )  # type: ignore

        logger.info(" ATLEAST REACHED HERE")
        response = await self.user_service.create_user(
            data=register_data, params=params
        )
        logger.info(response)
        result = response.json()
        logger.info(result)
        try:
            response.raise_for_status()
        except Exception as e:
            logger.error(e)
            raise WebServiceError(
                error_code=response.status_code,
                error=e,
                errors=WebServiceError.unpack(result),
            ) from e
        else:
            data = result["data"]
            logger.debug(data)

        return RegisterResponseModel(message="User successfuly registered")

    async def register(
        self, command: RegisterCommand
    ) -> RegisterResponseModel:
        try:
            register_method_handlers = {
                "instant": self.register_user,
            }
            handler = register_method_handlers[command.register_method]
            response = await handler(command=command)
            return response
        except KeyError as e:
            logger.error(e, exc_info=True)
            raise WebServiceError(
                title="invalid register method",
                description=f"invalid register method = {command.register_method}",
                error_severity="NONE_OPERATIONAL",
                error_code=400,
            )

    async def _login_password(self, command: LoginCommand) -> UserPayload:
        body = await command.request.json()
        request_body = dict(body)  # TODO change to pydantic validate model
        try:
            password = request_body["password"]
            identifier = request_body["identifier"]
        except KeyError:
            raise WebServiceError(
                title=f"invalid request body for login method {command.login_method}",
                error_code=400,
            )

        field = None
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        username_pattern = r"^[\w]+$"

        if re.match(email_pattern, identifier):
            field = "email"
        elif re.match(username_pattern, identifier):
            field = "username"

        if field is None:
            raise WebServiceError(
                title=f"invalid identifer for login method {command.login_method}",
                error_code=400,
            )

        response = await self.user_service.get_users(
            filters=[{"field": field, "value": identifier, "operator": "eq"}],
        )

        if not response.is_success:
            raise WebServiceError(  # TODO delete this and use default web client with custom exception
                title="user service response gave unexpected response",
                description="user service response was not successful, 'get' should always be successful in get many users context",
                error_code=500,
            )

        try:
            res = response.json()
            data = res["data"]
            if len(data) != 1:
                raise WebServiceError(
                    error_message=f"{field} '{identifier}' does not exists",
                    is_public=True,
                    error_code=401,
                )
            user = data[0]
            hashed_password = user["hashed_password"]
        except (KeyError, IndexError) as e:
            logger.error(e, exc_info=True)
            raise WebServiceError(
                title="failed to parse user repsonse",
                description="failed to parse user repsonse",
                error_code=500,
            )

        is_success = verify_password(password, hashed_password)
        if not is_success:
            raise WebServiceError(
                error_message="Invalid password",
                error_code=401,
                is_public=True,
            )
        try:
            user_payload = UserPayload.model_validate(user)
            return user_payload
        except ValidationError:
            raise WebServiceError(
                title="user payload failed to parse user", error_code=500
            )

    async def login_password(self, command: LoginCommand):
        user_payload = await self._login_password(command)
        logger.debug(user_payload)

        session_id_token = await self.token_service.generate_session_id_token()
        csrf_token = await self.token_service.generate_csrf_token()

        access_payload = AccessPayload.model_validate(
            self.internal_service_access
        )
        product_payload = ProductPayload(product_id=command.product_id)
        login_payload = LoginPayload(
            login_method="password",
            login_provider=None,
        )
        session_payload = SessionPayload(session_id=session_id_token)

        await self.user_active_session_service.create_user_session(
            session_key=session_id_token,
            user_set_key=self.get_user_sessions_key(user_payload.user_id),
            value=UserSessionData(
                last_activity=datetime_to_string(utcnow()),
                user_id=user_payload.user_id,
                product_id=command.product_id,
                extend_count=0,
                session_id=session_id_token,
                user_email=user_payload.user_email,
                user_username=user_payload.user_username,
                # expire_at=self.
                # ttl=self.session_ttl
            ).model_dump(),
            expire_at=self.session_ttl,
            product_set_key=self.get_product_sessions_key(command.product_id),
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

        session_token = await self.token_service.generate_session_token(
            SessionTokenPayload(
                product=product_payload,
                session=session_payload,
                user=user_payload,
            ),
            self.session_token_expire,
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

        response_data = {
            "tokens": {
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
            },
            "message": "Login successful",
        }

        _response = JSONResponse(
            content=response_data,
            headers=command.response.headers,
            status_code=200,
        )
        return _response

        # response_add_security_headers(command.response)
        # response_set_form_encoded_content_type(command.response)
        # response_add_redirect_location_header(command.response, "/")
        # urlencoded_content = urlencode(response_data)
        # _response = Response(
        #     content=urlencoded_content,
        #     media_type="application/x-www-form-urlencoded",
        #     headers=command.response.headers,
        #     status_code=200
        # )
        # return _response
        # return LoginResponseModel(
        #     # data=response_data,
        #     message="Login Successfully"
        # )

    async def login(
        self, command: LoginCommand
    ) -> LoginResponseModel | Response:
        try:
            login_method_handlers = {
                "password": self.login_password,
                # "oauth":None,
                # "totp": None
            }
            handler = login_method_handlers[command.login_method]
            response = await handler(command=command)
            return response
        except KeyError as e:
            logger.error(e, exc_info=True)
            raise WebServiceError(
                title="invalid login method(Optimistic)",
                description=f"invalid login method = {command.login_method}",
                error_severity="NONE_OPERATIONAL",
                error_code=400,
            )

    async def logout(
        self, command: LogoutCommand
    ) -> LogoutResponseModel | Response:
        csrf_token = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.CSRF_TOKEN.value
        )
        if csrf_token is not None:
            self.cookies_manager.delete_cookie(
                command.response, TokenKeyType.CSRF_TOKEN.value
            )

        session_id = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is not None:
            # revoke
            user_session_data = (
                await self.user_active_session_service.get_user_session(
                    session_id
                )
            )
            if user_session_data is not None:
                try:
                    user_session = UserSessionData.model_validate(
                        user_session_data
                    )
                except ValidationError:
                    logger.warning(
                        "failed to validate user session data, this should not happen"
                    )
                else:
                    user_sessions_key = self.get_user_sessions_key(
                        user_session.user_id
                    )

                    delete_user_session_response = await self.user_active_session_service.delete_user_session(
                        session_id
                    )
                    delete_user_from_user_sessions_response = await self.user_active_session_service.delete_user_session_from_user_sessions(
                        session_id, user_sessions_key
                    )
                    delete_empty_user_sessions_response = await self.user_active_session_service.delete_empty_user_sessions(
                        user_sessions_key
                    )

                    if user_session.product_id is not None:
                        product_sessions_key = self.get_product_sessions_key(
                            user_session.product_id
                        )
                        delete_user_from_product_sessions_response = await self.user_active_session_service.delete_user_session_from_product_sessions(
                            session_id, product_sessions_key
                        )
                        logger.debug(
                            f"""
                            Logout:
                                delete_user_session_response: {delete_user_session_response}
                                delete_user_from_user_sessions_response: {delete_user_from_user_sessions_response}
                                delete_empty_user_sessions_response: {delete_empty_user_sessions_response}
                                delete_user_from_product_sessions_response: {delete_user_from_product_sessions_response}
                            """
                        )
                    else:
                        logger.debug(
                            f"""
                            Logout:
                                delete_user_session_response: {delete_user_session_response}
                                delete_user_from_user_sessions_response: {delete_user_from_user_sessions_response}
                                delete_empty_user_sessions_response: {delete_empty_user_sessions_response}
                            """
                        )
            self.cookies_manager.delete_cookie(
                command.response, TokenKeyType.SESSION_ID_TOKEN.value
            )

        session_token_cookie = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.SESSION_TOKEN.value
        )
        if session_token_cookie is not None:
            # revoke
            self.cookies_manager.delete_cookie(
                command.response, TokenKeyType.SESSION_TOKEN.value
            )

        access_token_cookie = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.ACCESS_TOKEN.value
        )
        if access_token_cookie is not None:
            # revoke
            self.cookies_manager.delete_cookie(
                command.response, TokenKeyType.ACCESS_TOKEN.value
            )

        refresh_token_cookie = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.REFRESH_TOKEN.value
        )
        if refresh_token_cookie is not None:
            # revoke
            self.cookies_manager.delete_cookie(
                command.response, TokenKeyType.REFRESH_TOKEN.value
            )

        return LogoutResponseModel(message="Logged out successfully")

    async def _verify(self, command: VerifyCommand):
        verified_data = {}
        if command.verify_csrf_token:
            csrf_token = await self.verify_csrf_token(command.request)
            verified_data[TokenKeyType.CSRF_TOKEN.value] = csrf_token

        if command.verify_session_id_token:
            data = await self.verify_session_id_token(command.request)
            data = data.model_dump(
                exclude_defaults=False,
                exclude_none=False,
                exclude_unset=False,
            )
            verified_data[TokenKeyType.SESSION_ID_TOKEN.value] = data

        if command.verify_session_token:
            data = await self.verify_session_token(command.request)
            data = data.model_dump(
                exclude_defaults=False,
                exclude_none=False,
                exclude_unset=False,
            )
            verified_data[TokenKeyType.SESSION_TOKEN.value] = data

        if command.verify_access_token:
            data = await self.verify_access_token(command.request)
            data = data.model_dump(
                exclude_defaults=False,
                exclude_none=False,
                exclude_unset=False,
            )
            verified_data[TokenKeyType.ACCESS_TOKEN.value] = data

        if command.verify_refresh_token:
            data = await self.verify_refresh_token(command.request)
            data = data.model_dump(
                exclude_defaults=False,
                exclude_none=False,
                exclude_unset=False,
            )
            verified_data[TokenKeyType.REFRESH_TOKEN.value] = data

        return JSONResponse(content=verified_data, status_code=200)

    async def verify(self, command: VerifyCommand):
        verified_data = {}
        command.response.status_code = 401

        if command.verify_csrf_token:
            csrf_token = command.request.headers.get(
                CSRF_TOKEN_HEADER_KEY, None
            )
            if csrf_token is None:
                raise WebServiceError(
                    title="invalid request need csrf token header",
                    error_code=400,
                    description="CSRF token header is missing.",
                )

            if not isinstance(csrf_token, str):
                raise WebServiceError(
                    title="invalid request csrf token is not a string",
                    error_code=400,
                    description="invalid request csrf token is not a string",
                )

            csrf_token_cookie = self.cookies_manager.get_cookie(
                command.request, TokenKeyType.CSRF_TOKEN.value, None
            )

            if csrf_token_cookie is None:
                raise WebServiceError(
                    title="invalid request need csrf cookie",
                    error_code=401,
                    description="CSRF cookie is missing.",
                )

            if csrf_token != csrf_token_cookie:
                logger.warning(
                    "CSRF tokens do not match, might be malicious..."
                )
                # TODO blacklist ip
                self.cookies_manager.delete_cookie(
                    command.response, TokenKeyType.CSRF_TOKEN.value
                )
                command.response.status_code = 401
                return command.response

            verified_data[TokenKeyType.CSRF_TOKEN.value] = csrf_token

        if command.verify_session_id_token:
            session_id = self.cookies_manager.get_cookie(
                command.request, TokenKeyType.SESSION_ID_TOKEN.value
            )
            if session_id is None:
                raise WebServiceError(
                    title="invalid session id",
                    error_code=401,
                    description="session id cookie is missing.",
                )

            user_session_data = (
                await self.user_active_session_service.get_user_session(
                    session_id
                )
            )
            if user_session_data is None:
                self.cookies_manager.delete_cookie(
                    command.response, TokenKeyType.SESSION_ID_TOKEN.value
                )
                command.response.status_code = 401
                return command.response
            else:
                await self.user_active_session_service.update_user_session_expire(
                    session_id, self.session_ttl
                )

            try:
                user_session = UserSessionData.model_validate(
                    user_session_data
                )
            except ValidationError:
                logger.warning(
                    f"validation failure for user session data: {user_session_data}"
                )
            else:
                data = user_session.model_dump(
                    exclude_defaults=False,
                    exclude_none=False,
                    exclude_unset=False,
                )
                verified_data[TokenKeyType.SESSION_ID_TOKEN.value] = data

        if command.verify_session_token:
            session_token = self.cookies_manager.get_cookie(
                command.request, TokenKeyType.SESSION_TOKEN.value
            )
            if session_token is None:
                raise WebServiceError(
                    title="session token cookie does not exists",
                    error_code=401,
                )
            try:
                session_token_payload = (
                    await self.token_service.verify_session_token(
                        session_token
                    )
                )
            except Exception:
                self.cookies_manager.delete_cookie(
                    command.response, TokenKeyType.SESSION_TOKEN.value
                )
                command.response.status_code = 401
                return command.response
            else:
                if not isinstance(session_token_payload, dict):
                    session_token_payload = session_token_payload.model_dump(
                        exclude_defaults=False,
                        exclude_none=False,
                        exclude_unset=False,
                    )

                verified_data[TokenKeyType.SESSION_TOKEN.value] = (
                    session_token_payload
                )

        if command.verify_access_token:
            access_token = self.cookies_manager.get_cookie(
                command.request, TokenKeyType.ACCESS_TOKEN.value
            )
            if access_token is None:
                raise WebServiceError(
                    title="access token cookie does not exists", error_code=401
                )
            try:
                access_token_payload = (
                    await self.token_service.verify_access_token(access_token)
                )
            except Exception:
                self.cookies_manager.delete_cookie(
                    command.response, TokenKeyType.ACCESS_TOKEN.value
                )
                command.response.status_code = 401
                return command.response
            else:
                if not isinstance(access_token_payload, dict):
                    access_token_payload = access_token_payload.model_dump(
                        exclude_defaults=False,
                        exclude_none=False,
                        exclude_unset=False,
                    )
                verified_data[TokenKeyType.ACCESS_TOKEN.value] = (
                    access_token_payload
                )

        if command.verify_refresh_token:
            refresh_token = self.cookies_manager.get_cookie(
                command.request, TokenKeyType.REFRESH_TOKEN.value
            )
            if refresh_token is None:
                raise WebServiceError(
                    title="access token cookie does not exists", error_code=401
                )
            try:
                refresh_token_payload = (
                    await self.token_service.verify_refresh_token(
                        refresh_token
                    )
                )
            except Exception:
                self.cookies_manager.delete_cookie(
                    command.response, TokenKeyType.REFRESH_TOKEN.value
                )
                command.response.status_code = 401
                return command.response
            else:
                if not isinstance(refresh_token_payload, dict):
                    refresh_token_payload = refresh_token_payload.model_dump(
                        exclude_defaults=False,
                        exclude_none=False,
                        exclude_unset=False,
                    )
                verified_data[TokenKeyType.REFRESH_TOKEN.value] = (
                    refresh_token_payload
                )

        return JSONResponse(content=verified_data, status_code=200)

    async def verify_csrf_token(self, request: Request) -> str:
        logger.info("verifying csrf tokens...")
        csrf_token = request.headers.get(CSRF_TOKEN_HEADER_KEY, None)

        if csrf_token is None:
            raise WebServiceError(
                title="invalid request need csrf token header",
                error_code=400,
                description="CSRF token header is missing.",
            )

        if not isinstance(csrf_token, str):
            raise WebServiceError(
                title="invalid request csrf token is not a string",
                error_code=400,
                description="invalid request csrf token is not a string",
            )

        csrf_token_cookie = self.cookies_manager.get_cookie(
            request, TokenKeyType.CSRF_TOKEN.value, None
        )

        if csrf_token_cookie is None:
            raise WebServiceError(
                title="invalid request need csrf cookie",
                error_code=401,
                description="CSRF cookie is missing.",
            )

        if csrf_token != csrf_token_cookie:
            logger.warning("CSRF tokens do not match, might be malicious...")
            raise WebServiceError(
                title="CSRF tokens do not match",
                description=f"CSRF tokens do not match. Header CSRF token: {csrf_token}, Cookie CSRF token: {csrf_token_cookie}",
                error_code=401,
            )
            # TODO blacklist ip
        return csrf_token

    async def verify_session_id_token(
        self, request: Request
    ) -> UserSessionData:
        return await self.verify_active_session(request)

    async def verify_active_session(self, request: Request) -> UserSessionData:
        session_id = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is None:
            raise WebServiceError(
                error_message="session id cookie does not exists",
                error_code=401,
            )
        user_session_data = (
            await self.user_active_session_service.get_user_session(session_id)
        )
        if user_session_data is None:
            raise WebServiceError(
                error_message="user session does not exists", error_code=401
            )
        try:
            user_session = UserSessionData.model_validate(user_session_data)
        except ValidationError as e:
            raise WebServiceError(
                title="failed to validate user session data model",
                error_code=500,
                error_message=f"validation failure for user session data: {user_session_data}",
            ) from e
        else:
            return user_session

    async def verify_session_token(
        self, request: Request
    ) -> SessionTokenPayload:
        session_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_TOKEN.value
        )
        if session_token is None:
            raise WebServiceError(
                title="session token cookie does not exists", error_code=401
            )
        try:
            session_token_payload = (
                await self.token_service.verify_session_token(
                    session_token, raise_exception=True
                )
            )
            return session_token_payload  # type: ignore
        except ValidationError as e:
            raise WebServiceError(
                title="session token invalid structure", error_code=500
            ) from e
        except Exception as e:
            raise WebServiceError(
                title="session token cookie is invalid", error_code=401
            ) from e

    async def verify_access_token(
        self, request: Request
    ) -> AccessTokenPayload:
        access_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.ACCESS_TOKEN.value
        )
        if access_token is None:
            raise WebServiceError(
                title="access token cookie does not exists", error_code=401
            )
        try:
            access_token_payload = (
                await self.token_service.verify_access_token(
                    access_token, raise_exception=True
                )
            )
            return access_token_payload  # type: ignore

        except ValidationError as e:
            raise WebServiceError(
                title="access token invalid structure", error_code=500
            ) from e

        except Exception as e:
            raise WebServiceError(
                title="session token cookie is invalid", error_code=401
            ) from e

    async def verify_refresh_token(
        self, request: Request
    ) -> RefreshTokenPayload:
        refresh_token_cookie = self.cookies_manager.get_cookie(
            request, TokenKeyType.REFRESH_TOKEN.value
        )
        if refresh_token_cookie is None:
            raise WebServiceError(
                title="refresh token cookie does not exists", error_code=401
            )
        try:
            refresh_token_payload = (
                await self.token_service.verify_refresh_token(
                    refresh_token=refresh_token_cookie, raise_exception=True
                )
            )
            return refresh_token_payload  # type: ignore
        except ValidationError as e:
            raise WebServiceError(
                title="refresh token invalid structure", error_code=500
            ) from e

        except Exception as e:
            raise WebServiceError(
                title="refresh token cookie is invalid", error_code=401
            ) from e

    async def whoami(self, command: WhoAmICommand):
        user_session = await self.verify_active_session(command.request)
        user_response = await self.user_service.get_user(user_session.user_id)
        if user_response.status_code != 200:
            raise WebServiceError(
                error_code=500,
                error_message="user does not exists ,but does exists in active session",
            )

        content = user_response.json()
        return JSONResponse(status_code=200, content=content)

    async def refresh_csrf_token(
        self, command: RefreshCommand, request: Request, response: Response
    ) -> str | None:
        csrf_token_expire = await self.refresh_session(
            command, request, response
        )
        if csrf_token_expire is not None:
            csrf_token = await self.token_service.generate_csrf_token()
            self.cookies_manager.set_cookie(
                response=response,
                key=TokenKeyType.CSRF_TOKEN.value,
                value=csrf_token,
                expire=csrf_token_expire,
            )
            return csrf_token
        else:
            csrf_token = self.cookies_manager.get_cookie(
                request, TokenKeyType.CSRF_TOKEN.value
            )
            if csrf_token is not None:
                self.cookies_manager.delete_cookie(
                    response, TokenKeyType.CSRF_TOKEN.value
                )

    async def refresh_session(
        self, command: RefreshCommand, request: Request, response: Response
    ) -> int | None:
        session_id = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is not None:
            user_session = (
                await self.user_active_session_service.get_user_session(
                    session_id
                )
            )
            if user_session is not None:
                ttl = await self.user_active_session_service.get_user_session_expire(
                    session_id
                )
                return ttl

        session_token_payload = await self.refresh_session_token(
            command, request, response
        )
        if session_token_payload is not None:
            await self.user_active_session_service.create_user_session(
                session_key=session_token_payload.session.session_id,
                user_set_key=self.get_user_sessions_key(
                    session_token_payload.user.user_id
                ),
                value=UserSessionData(
                    last_activity=datetime_to_string(utcnow()),
                    user_id=session_token_payload.user.user_id,
                    product_id=command.product_id,
                    extend_count=0,
                    session_id=session_token_payload.session.session_id,
                    user_email=session_token_payload.user.user_email,
                    user_username=session_token_payload.user.user_username,
                ).model_dump(),
                expire_at=self.session_ttl,
                product_set_key=self.get_product_sessions_key(
                    session_token_payload.product.product_id
                ),
            )
            self.cookies_manager.set_cookie(
                response=response,
                key=TokenKeyType.SESSION_ID_TOKEN.value,
                value=session_token_payload.session.session_id,
                expire=self.session_id_token_expire,
            )
            return self.session_ttl

        if session_id is not None:
            self.cookies_manager.delete_cookie(
                response, TokenKeyType.SESSION_ID_TOKEN.value
            )

        return None

    async def refresh_session_token(
        self, command: RefreshCommand, request: Request, response: Response
    ) -> SessionTokenPayload | None:
        session_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_TOKEN.value
        )
        if session_token is not None:
            try:
                session_token_payload: SessionTokenPayload = (
                    await self.token_service.verify_session_token(
                        session_token
                    )
                )  # type: ignore
                return session_token_payload  # valid so its ok its can be used
            except Exception:  # not valid
                pass

        access_token_payload = await self.refresh_access_token(
            command, request, response
        )
        if access_token_payload is not None:
            session_id = await self.token_service.generate_session_id_token()
            payload = SessionTokenPayload(
                product=access_token_payload.product,
                session=SessionPayload(
                    session_id=session_id,
                ),
                user=access_token_payload.user,
            )
            new_session_token = (
                await self.token_service.generate_session_token(
                    payload=payload,
                    expiration=self.session_token_expire,
                )
            )
            self.cookies_manager.set_cookie(
                response=response,
                key=TokenKeyType.SESSION_TOKEN.value,
                value=new_session_token,
                expire=self.session_token_expire,
            )
            return payload

        if session_token is not None:
            self.cookies_manager.delete_cookie(
                response, TokenKeyType.SESSION_TOKEN.value
            )

        return None

    async def refresh_access_token(
        self, command: RefreshCommand, request: Request, response: Response
    ) -> AccessTokenPayload | None:
        access_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.ACCESS_TOKEN.value
        )
        if access_token is not None:
            try:
                access_token_payload: AccessTokenPayload = (
                    await self.token_service.verify_access_token(access_token)
                )  # type: ignore
                return access_token_payload
            except Exception:  # invalid access token
                pass

        refresh_token_payload = await self.refresh_refresh_token(
            command, request, response
        )
        if refresh_token_payload:
            access_payload = AccessPayload.model_validate(
                self.internal_service_access
            )
            payload = AccessTokenPayload(
                access=access_payload,
                product=refresh_token_payload.product,
                user=refresh_token_payload.user,
            )
            new_access_token = await self.token_service.generate_access_token(
                payload, self.access_token_expire
            )
            self.cookies_manager.set_cookie(
                response=response,
                key=TokenKeyType.ACCESS_TOKEN.value,
                value=new_access_token,
                expire=self.access_token_expire,
            )
            return payload

        if access_token is not None:
            self.cookies_manager.delete_cookie(
                response, TokenKeyType.ACCESS_TOKEN.value
            )

        return None

    async def refresh_refresh_token(
        self, command: RefreshCommand, request: Request, response: Response
    ) -> RefreshTokenPayload | None:
        refresh_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.REFRESH_TOKEN.value
        )
        if refresh_token is not None:
            try:
                refresh_token_payload: RefreshTokenPayload = (
                    await self.token_service.verify_refresh_token(
                        refresh_token=refresh_token, raise_exception=False
                    )
                )  # type: ignore
                return refresh_token_payload
            except Exception:
                pass

        if refresh_token is not None:
            self.cookies_manager.delete_cookie(
                response, TokenKeyType.REFRESH_TOKEN.value
            )

        return None

    async def refresh(self, command: RefreshCommand):
        csrf = await self.refresh_csrf_token(
            command, command.request, command.response
        )
        command.response.status_code = 200
        if csrf is None:
            command.response.status_code = 401
        return command.response

    async def get_user_authentication_data(
        self, command: GetUserAuthenticationDataCommand
    ):
        # result = await self.user_active_session_service.get_user_sessions(session_key=command.user_id)
        # return result
        pass

    async def get_product_authentication_data(
        self, command: GetProductAuthenticationDataCommand
    ):
        # product_key = command.user_id
        # result = await self.user_active_session_service.get_product_sessions(product_key)
        # return result
        pass

    async def confirm_registration(self, token: str):
        pass

    async def on_unexpected_behavior(self):
        logger.info("UNEXCEPTED BEHAVIOR")

    async def encrypt_user_id(self, user_id: str) -> str:
        user_id_bytes = user_id.encode("utf-8")
        encrypted_id = self.cipher_suite.encrypt(user_id_bytes)
        return encrypted_id.decode("utf-8")

    async def decrypt_user_id(self, encrypted_id: str) -> str:
        try:
            encrypted_id_bytes = encrypted_id.encode("utf-8")
            decrypted_id = self.cipher_suite.decrypt(encrypted_id_bytes)
            return decrypted_id.decode("utf-8")
        except Exception:
            raise WebServiceError(
                error_code=400, detail="Invalid encrypted ID"
            )
