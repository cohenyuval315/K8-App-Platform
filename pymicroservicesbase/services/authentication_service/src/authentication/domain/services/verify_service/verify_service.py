from fastapi import Request, Response
from pydantic import ValidationError
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.verify_command import (
    VerifyCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.revocation.revocation_service import (
    RevocationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_active_session_service import (
    UserActiveSessionService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session import (
    UserSessionData,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.tokens_service import (
    TokenService,
)
from pymicroservicesbase.services.authentication_service.src.cookies.cookies_manager import (
    CookiesManager,
)
from pymicroservicesbase.shared.constants.headers import CSRF_TOKEN_HEADER_KEY
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType
from pymicroservicesbase.services.authentication_service.logger import logger


class VerifyService:
    def __init__(
        self,
        cookies_manager: CookiesManager,
        user_active_session_service: UserActiveSessionService,
        token_service: TokenService,
        revocation_service: RevocationService,
        verify_csrf_token: bool = True,
        verify_session_id_token: bool = True,
        verify_access_token: bool = True,
        verify_refresh_token: bool = True,
        verify_session_token: bool = True,
    ):
        self.cookies_manager = cookies_manager
        self.user_active_session_service = user_active_session_service
        self.token_service = token_service
        self.revocation_service = revocation_service

        self.verify_csrf_token = verify_csrf_token
        self.verify_session_id_token = verify_session_id_token
        self.verify_access_token = verify_access_token
        self.verify_refresh_token = verify_refresh_token
        self.verify_session_token = verify_session_token

    async def verify(self, command: VerifyCommand):
        cookies_to_delete = []

        if self.verify_csrf_token:
            cookies_to_delete.append(TokenKeyType.CSRF_TOKEN.value)
            logger.info("Starting CSRF token verification.")
            try:
                await self._verify_csrf_token(command.request)
                logger.info("CSRF token verification successful.")
            except WebServiceError:
                logger.error("CSRF token verification failed.")
                csrf_header_token = command.request.headers.get(
                    CSRF_TOKEN_HEADER_KEY, None
                )
                if csrf_header_token:
                    revoke_header_response = (
                        await self.revocation_service.revoke(csrf_header_token)
                    )
                    logger.debug(
                        f"Revocation response for CSRF token: {revoke_header_response}"
                    )
                else:
                    logger.warning(
                        f"csrf token header should not be None in this point.... {csrf_header_token}"
                    )

                await self._revoke_and_delete_cookies(
                    command, cookies_to_delete
                )
                return Response(
                    status_code=401, headers=command.response.headers
                )

        if self.verify_session_id_token:
            cookies_to_delete.append(TokenKeyType.SESSION_ID_TOKEN.value)
            logger.info("Starting session ID token verification.")
            try:
                await self._verify_session_id_token(command.request)
                logger.info("Session ID token verification successful.")
            except WebServiceError:
                logger.error("Session ID token verification failed.")
                await self._revoke_and_delete_cookies(
                    command, cookies_to_delete
                )
                return Response(
                    status_code=401, headers=command.response.headers
                )

        if self.verify_session_token:
            cookies_to_delete.append(TokenKeyType.SESSION_TOKEN.value)
            logger.info("Starting session token verification.")
            try:
                await self._verify_session_token(command.request)
                logger.info("Session token verification successful.")
            except WebServiceError:
                logger.error("Session token verification failed.")
                await self._revoke_and_delete_cookies(
                    command, cookies_to_delete
                )
                return Response(
                    status_code=401, headers=command.response.headers
                )

        if self.verify_access_token:
            cookies_to_delete.append(TokenKeyType.ACCESS_TOKEN.value)
            logger.info("Starting access token verification.")
            try:
                await self._verify_access_token(command.request)
                logger.info("Access token verification successful.")
            except WebServiceError:
                logger.error("Access token verification failed.")
                await self._revoke_and_delete_cookies(
                    command, cookies_to_delete
                )
                return Response(
                    status_code=401, headers=command.response.headers
                )

        if self.verify_refresh_token:
            cookies_to_delete.append(TokenKeyType.REFRESH_TOKEN.value)
            logger.info("Starting refresh token verification.")
            try:
                await self._verify_refresh_token(command.request)
                logger.info("Refresh token verification successful.")
            except WebServiceError:
                logger.error("Refresh token verification failed.")
                await self._revoke_and_delete_cookies(
                    command, cookies_to_delete
                )
                return Response(
                    status_code=401, headers=command.response.headers
                )

        logger.info("All verified successfully.")
        return Response(status_code=200, headers=command.response.headers)

    async def _revoke_and_delete_cookies(
        self, command: VerifyCommand, cookies: list
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

    async def _verify_csrf_token(self, request: Request):
        logger.debug("Verifying CSRF token header.")
        csrf_header_token = request.headers.get(CSRF_TOKEN_HEADER_KEY, None)
        if csrf_header_token is None:
            logger.error("CSRF token header is missing.")
            raise WebServiceError(
                error_code=400,
                error_message="CSRF token header is missing.",
            )

        csrf_token_cookie = self.cookies_manager.get_cookie(
            request, TokenKeyType.CSRF_TOKEN.value, None
        )
        if csrf_token_cookie is None:
            logger.error("CSRF cookie is missing.")
            raise WebServiceError(
                error_code=401,
                error_message="CSRF cookie is missing.",
            )

        if csrf_header_token != csrf_token_cookie:
            logger.warning("CSRF tokens do not match, might be malicious...")
            raise WebServiceError(
                error_message="CSRF tokens do not match", error_code=401
            )

    async def _verify_session_id_token(
        self, request: Request
    ) -> UserSessionData:
        logger.debug("Verifying session ID token.")
        return await self.__verify_active_session(request)

    async def __verify_active_session(
        self, request: Request
    ) -> UserSessionData:
        logger.debug("Verifying active session using session ID.")
        session_id = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is None:
            logger.error("Session ID cookie does not exist.")
            raise WebServiceError(
                error_message="session id cookie does not exists",
                error_code=401,
            )
        user_session_data = (
            await self.user_active_session_service.get_user_session(session_id)
        )
        if user_session_data is None:
            logger.error("User session does not exist.")
            raise WebServiceError(
                error_message="user session does not exists", error_code=401
            )
        try:
            user_session = UserSessionData.model_validate(user_session_data)
            logger.debug(
                f"User session validated successfully. result {user_session}"
            )
            return user_session
        except ValidationError as e:
            logger.error(
                f"Validation failure for user session data: {user_session_data}"
            )
            raise WebServiceError(
                error_code=500,
                error_message=f"validation failure for user session data: {user_session_data}",
            ) from e

    async def _verify_session_token(self, request: Request):
        logger.debug("Verifying session token.")
        session_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.SESSION_TOKEN.value
        )
        if session_token is None:
            logger.error("Session token cookie does not exist.")
            raise WebServiceError(
                title="session token cookie does not exists", error_code=401
            )
        try:
            session_token_payload = (
                await self.token_service.verify_session_token(session_token)
            )
            logger.debug(
                f"Session token verified successfully. result:{session_token_payload}"
            )

        except ValidationError as e:
            logger.error(f"Session token structure invalid: {str(e)}")
            raise WebServiceError(
                title="session token invalid structure", error_code=500
            ) from e
        except Exception as e:
            logger.error(f"Session token cookie is invalid: {str(e)}")
            raise WebServiceError(
                title="session token cookie is invalid", error_code=401
            ) from e

    async def _verify_access_token(self, request: Request):
        logger.debug("Verifying access token.")
        access_token = self.cookies_manager.get_cookie(
            request, TokenKeyType.ACCESS_TOKEN.value
        )
        if access_token is None:
            logger.error("Access token cookie does not exist.")
            raise WebServiceError(
                title="access token cookie does not exists", error_code=401
            )
        try:
            access_token_payload = (
                await self.token_service.verify_access_token(access_token)
            )
            logger.debug(
                f"Access token verified successfully. result: {access_token_payload}"
            )

        except ValidationError as e:
            logger.error(f"Access token structure invalid: {str(e)}")
            raise WebServiceError(
                title="access token invalid structure", error_code=500
            ) from e

        except Exception as e:
            logger.error(f"Access token cookie is invalid: {str(e)}")
            raise WebServiceError(
                title="session token cookie is invalid", error_code=401
            ) from e

    async def _verify_refresh_token(self, request: Request):
        logger.debug("Verifying refresh token.")
        refresh_token_cookie = self.cookies_manager.get_cookie(
            request, TokenKeyType.REFRESH_TOKEN.value
        )
        if refresh_token_cookie is None:
            logger.error("Refresh token cookie does not exist.")
            raise WebServiceError(
                title="refresh token cookie does not exists", error_code=401
            )
        try:
            refresh_token_payload = (
                await self.token_service.verify_refresh_token(
                    refresh_token=refresh_token_cookie
                )
            )
            logger.debug(
                f"Refresh token verified successfully. result: {refresh_token_payload}"
            )
        except ValidationError as e:
            logger.error(f"Refresh token structure invalid: {str(e)}")
            raise WebServiceError(
                title="refresh token invalid structure", error_code=500
            ) from e

        except Exception as e:
            logger.error(f"Refresh token cookie is invalid: {str(e)}")
            raise WebServiceError(
                title="refresh token cookie is invalid", error_code=401
            ) from e
