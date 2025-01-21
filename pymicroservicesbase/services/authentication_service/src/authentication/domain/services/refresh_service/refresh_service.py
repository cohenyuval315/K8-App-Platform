from typing import Type, TypeVar
from fastapi import Response
from pydantic import ValidationError
from pymicroservicesbase.services.api_gateway_service.src.app import (
    WebServiceError,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.refresh.refresh_command import (
    RefreshCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.revocation.revocation_service import (
    RevocationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.session_key_manager import (
    SessionKeyManager,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_active_session_service import (
    UserActiveSessionService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session import (
    UserSessionData,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads import (
    SessionPayload,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads.access_payload import (
    AccessPayload,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads.access_token_payload import (
    AccessTokenPayload,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads.refresh_token_payload import (
    RefreshTokenPayload,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads.session_token_payload import (
    SessionTokenPayload,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.tokens_service import (
    TokenService,
)
from pymicroservicesbase.services.authentication_service.src.cookies.cookies_manager import (
    CookiesManager,
)
from pymicroservicesbase.shared.constants.headers import LOCATION_HEADER_KEY
from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_string,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType
from pymicroservicesbase.shared.constants.media_type import MediaType
from pymicroservicesbase.services.authentication_service.logger import logger
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class RefreshService:
    def __init__(
        self,
        session_key_manager: SessionKeyManager,
        revocation_service: RevocationService,
        cookies_manager: CookiesManager,
        token_service: TokenService,
        user_active_session_service: UserActiveSessionService,
        internal_service_access,
        refresh_token_expire,
        access_token_expire,
        session_token_expire,
        session_id_token_expire,
        csrf_token_expire,
        session_ttl,
        refresh_csrf_token_with_session_id_token,
        refresh_session_id_token_with_session_token,
        refresh_session_token_with_access_token,
        refresh_access_token_with_refresh_token,
    ):
        self.cookies_manager = cookies_manager
        self.token_service = token_service
        self.user_active_session_service = user_active_session_service
        self.session_key_manager = session_key_manager
        self.revocation_service = revocation_service

        self.internal_service_access = internal_service_access
        self.refresh_token_expire = refresh_token_expire
        self.access_token_expire = access_token_expire
        self.session_token_expire = session_token_expire
        self.session_id_token_expire = session_id_token_expire
        self.csrf_token_expire = csrf_token_expire
        self.session_ttl = session_ttl

        self.refresh_csrf_token_with_session_id_token = (
            refresh_csrf_token_with_session_id_token
        )
        self.refresh_session_id_token_with_session_token = (
            refresh_session_id_token_with_session_token
        )
        self.refresh_session_token_with_access_token = (
            refresh_session_token_with_access_token
        )
        self.refresh_access_token_with_refresh_token = (
            refresh_access_token_with_refresh_token
        )

    async def refresh(self, command: RefreshCommand):
        cookies_to_delete = [TokenKeyType.CSRF_TOKEN.value]
        logger.info("Starting refresh process...")

        if self.refresh_csrf_token_with_session_id_token:
            cookies_to_delete.append(TokenKeyType.SESSION_ID_TOKEN.value)
            try:
                user_session, ttl = await self._verify_session_id_token(
                    command
                )
                logger.info(
                    "CSRF token refreshed successfully for a live session."
                )
                logger.debug(f"User session details: {user_session}")
            except WebServiceError as e:
                logger.error(f"Failed to refresh CSRF token: {e}")
            else:
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.CSRF_TOKEN.value,
                    await self.token_service.generate_csrf_token(),
                    ttl,
                )
                return Response(
                    status_code=200,
                    headers=command.response.headers,
                    media_type=MediaType.JSON,
                    content={
                        "message": "Refreshed live user session successfully.",
                        "method": TokenKeyType.SESSION_ID_TOKEN.value,
                    },
                )

        if self.refresh_session_id_token_with_session_token:
            cookies_to_delete.append(TokenKeyType.SESSION_TOKEN.value)
            try:
                session_token_payload = await self._verify_session_token(
                    command
                )
                logger.info("Session ID token refreshed successfully.")
                logger.debug(f"Session token payload: {session_token_payload}")
            except WebServiceError as e:
                logger.error(f"Failed to refresh session ID token: {e}")
            else:
                ttl = await self._create_active_session_from_session_token_payload(
                    session_token_payload
                )
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.CSRF_TOKEN.value,
                    await self.token_service.generate_csrf_token(),
                    ttl,
                )
                return Response(
                    headers=command.response.headers,
                    status_code=200,
                    media_type=MediaType.JSON,
                    content={
                        "message": "Refreshed live user session successfully.",
                        "method": TokenKeyType.SESSION_TOKEN.value,
                    },
                )

        if self.refresh_session_token_with_access_token:
            cookies_to_delete.append(TokenKeyType.ACCESS_TOKEN.value)
            try:
                access_token_payload = await self._verify_access_token(command)
                logger.info("Session token refreshed with access token.")
                logger.debug(f"Access token payload: {access_token_payload}")
            except WebServiceError as e:
                logger.error(
                    f"Failed to refresh session token with access token: {e}"
                )
            else:
                (session_token_payload, session_token) = (
                    await self._create_session_token_from_access_token_payload(
                        access_token_payload
                    )
                )
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.SESSION_TOKEN.value,
                    session_token,
                    self.session_token_expire,
                )
                ttl = await self._create_active_session_from_session_token_payload(
                    session_token_payload
                )
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.CSRF_TOKEN.value,
                    await self.token_service.generate_csrf_token(),
                    ttl,
                )
                return Response(
                    headers=command.response.headers,
                    status_code=200,
                    media_type=MediaType.JSON,
                    content={
                        "message": "Refreshed live user session successfully.",
                        "method": TokenKeyType.ACCESS_TOKEN.value,
                    },
                )

        if self.refresh_access_token_with_refresh_token:
            cookies_to_delete.append(TokenKeyType.REFRESH_TOKEN.value)
            try:
                refresh_token_payload = await self._verify_refresh_token(
                    command
                )
                logger.info("Access token refreshed with refresh token.")
                logger.debug(f"Refresh token payload: {refresh_token_payload}")
            except WebServiceError as e:
                logger.error(f"Failed to refresh with refresh token: {e}")
            else:
                (access_token_payload, access_token) = (
                    await self._create_access_token_from_refresh_token_payload(
                        refresh_token_payload
                    )
                )
                (session_token_payload, session_token) = (
                    await self._create_session_token_from_access_token_payload(
                        access_token_payload
                    )
                )
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.ACCESS_TOKEN.value,
                    access_token,
                    self.access_token_expire,
                )
                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.SESSION_TOKEN.value,
                    session_token,
                    self.session_token_expire,
                )
                ttl = await self._create_active_session_from_session_token_payload(
                    session_token_payload
                )

                self.cookies_manager.set_cookie(
                    command.response,
                    TokenKeyType.CSRF_TOKEN.value,
                    await self.token_service.generate_csrf_token(),
                    ttl,
                )

                return Response(
                    headers=command.response.headers,
                    status_code=200,
                    media_type=MediaType.JSON,
                    content={
                        "message": "Refreshed live user session successfully.",
                        "method": TokenKeyType.REFRESH_TOKEN.value,
                    },
                )
        logger.warning("Session ended, redirecting to login.")
        command.response.headers.append(LOCATION_HEADER_KEY, "/login")
        await self._revoke_and_delete_cookies(command, cookies_to_delete)
        return Response(
            headers=command.response.headers,
            media_type=MediaType.JSON,
            status_code=401,
            content={"message": "Session ended, redirecting to login."},
        )

    async def _verify_session_id_token(self, command: RefreshCommand):
        session_id = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is None:
            logger.error("Session ID does not exist.")
            raise WebServiceError(
                error_code=400, error_message="session id doesnt not exists"
            )

        logger.info(f"Verifying session ID: {session_id}")
        user_session = await self.user_active_session_service.get_user_session(
            session_id
        )

        if user_session is None:
            logger.error(
                f"User session does not exist for session ID: {session_id}"
            )
            raise WebServiceError(
                error_code=400,
                error_message=f"user session doesnt not exists for {session_id}",
            )

        logger.debug(f"Retrieved user session: {user_session}")
        ttl_left = (
            await self.user_active_session_service.get_user_session_expire(
                session_id
            )
        )
        logger.debug(f"TTL left for session ID {session_id}: {ttl_left}")

        try:
            user_session_data = UserSessionData.model_validate(user_session)
            logger.debug(f"User Session Data: {user_session_data}")

        except ValidationError:
            logger.error(
                f"Failed to parse user session data for session ID {session_id}"
            )
            raise WebServiceError(
                error_code=500,
                error_message=f"failed to parse user session data {user_session}",
            )
        else:
            logger.info(f"Session ID {session_id} verified successfully.")
            response = await self.user_active_session_service.update_user_session_expire(
                self.session_key_manager.get_user_sessions_key(
                    user_session_data.user_id
                ),
                self.session_ttl,
            )
            logger.debug(f"Updated session TTL. Response: {response}")

        return (user_session_data, self.session_ttl)

    async def _verify_token(
        self, command: RefreshCommand, token_key: str, model: Type[T]
    ) -> T:
        logger.info(f"Starting token verification for token key: {token_key}")
        token = self.cookies_manager.get_cookie(command.request, token_key)
        if token is None:
            logger.error(
                f"{token_key} token does not exist in the request cookies."
            )
            raise WebServiceError(
                error_message=f"{token_key} token does not exists",
                error_code=400,
            )
        logger.debug(f"Retrieved {token_key} token: {token}")
        try:
            payload = await self.token_service._verify_jwt_token(token)
            logger.debug(f"Decoded JWT payload for {token_key}: {payload}")
        except Exception as e:
            logger.error(f"Failed to verify {token_key} token: {str(e)}")
            raise WebServiceError(
                error_message="invalid session token", error_code=400
            ) from e

        try:
            token_payload = model.model_validate(payload)
            logger.info(f"Successfully validated {token_key} token structure.")
            return token_payload
        except ValidationError as e:
            logger.error(
                f"Invalid structure for {token_key}. Payload: {payload}. Error: {e}"
            )
            raise WebServiceError(
                error_message=f"invalid structure {token_key} {payload}",
                error_code=400,
            ) from e

    async def _verify_access_token(
        self, command: RefreshCommand
    ) -> AccessTokenPayload:
        return await self._verify_token(
            command, TokenKeyType.ACCESS_TOKEN.value, AccessTokenPayload
        )

    async def _verify_session_token(
        self, command: RefreshCommand
    ) -> SessionTokenPayload:
        return await self._verify_token(
            command, TokenKeyType.SESSION_TOKEN.value, SessionTokenPayload
        )

    async def _verify_refresh_token(
        self, command: RefreshCommand
    ) -> RefreshTokenPayload:
        return await self._verify_token(
            command, TokenKeyType.REFRESH_TOKEN.value, RefreshTokenPayload
        )

    async def _revoke_and_delete_cookies(
        self, command: RefreshCommand, cookies: list
    ):
        for cookie_key in cookies:
            logger.debug(
                f"Processing cookie revocation and deletion for token: {cookie_key}"
            )
            cookie = self.cookies_manager.get_cookie(
                command.request, cookie_key
            )
            if cookie is not None:
                logger.debug(f"Revoking cookie: {cookie_key}...")
                revoke_cookie_response = await self.revocation_service.revoke(
                    cookie
                )
                logger.debug(
                    f"Revocation response for {cookie_key}: {revoke_cookie_response}"
                )
                self.cookies_manager.delete_cookie(
                    command.response, cookie_key
                )
                logger.info(f"Cookie {cookie_key} deleted successfully.")
            else:
                logger.warning(
                    f"Cookie {cookie_key} not found, skipping deletion."
                )

    async def _create_session_token_from_access_token_payload(
        self, access_token_payload: AccessTokenPayload
    ):
        session_id_token = await self.token_service.generate_session_id_token()
        session_token_payload = SessionTokenPayload(
            product=access_token_payload.product,
            session=SessionPayload(session_id=session_id_token),
            user=access_token_payload.user,
        )
        session_token = await self.token_service.generate_session_token(
            payload=session_token_payload, expiration=self.session_token_expire
        )
        return (session_token_payload, session_token)

    async def _create_active_session_from_session_token_payload(
        self, session_token_payload: SessionTokenPayload
    ):
        user_session_data = UserSessionData(
            session_id=session_token_payload.session.session_id,
            product_id=session_token_payload.product.product_id,
            extend_count=0,
            last_activity=datetime_to_string(utcnow()),
            user_email=session_token_payload.user.user_email,
            user_username=session_token_payload.user.user_username,
            user_id=session_token_payload.user.user_id,
        ).model_dump()

        expired_at = self.session_ttl
        response = await self.user_active_session_service.create_user_session(
            session_key=session_token_payload.session.session_id,
            user_set_key=session_token_payload.user.user_id,
            expire_at=expired_at,
            product_set_key=session_token_payload.product.product_id,
            value=user_session_data,
        )
        logger.debug(f"Create User Session Response: {response}")
        return expired_at

    async def _create_access_token_from_refresh_token_payload(
        self, refresh_token_payload: RefreshTokenPayload
    ):
        access_token_payload = AccessTokenPayload(
            access=AccessPayload.model_validate(self.internal_service_access),
            product=refresh_token_payload.product,
            user=refresh_token_payload.user,
        )
        access_token = await self.token_service.generate_access_token(
            expiration=self.access_token_expire, payload=access_token_payload
        )
        return (access_token_payload, access_token)
