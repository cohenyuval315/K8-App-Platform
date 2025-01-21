from fastapi import Response
from pydantic import ValidationError
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.logout.logout_command import (
    LogoutCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.revocation.revocation_service import (
    RevocationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.session_key_manager import (
    SessionKeyManager,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session import (
    UserSessionData,
)
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType
from pymicroservicesbase.services.authentication_service.logger import logger
from pymicroservicesbase.shared.constants.media_type import MediaType


class LogoutService:
    def __init__(
        self,
        cookies_manager,
        session_key_manager: SessionKeyManager,
        user_active_session_service,
        revocation_service: RevocationService,
    ):
        self.cookies_manager = cookies_manager
        self.user_active_session_service = user_active_session_service
        self.session_key_manager = session_key_manager
        self.revocation_service = revocation_service

    async def logout(self, command: LogoutCommand):
        logger.info("Logout process started for the request.")
        token_keys = [
            TokenKeyType.CSRF_TOKEN.value,
            TokenKeyType.SESSION_TOKEN.value,
            TokenKeyType.ACCESS_TOKEN.value,
            TokenKeyType.REFRESH_TOKEN.value,
        ]
        for token_key in token_keys:
            await self._revoke_and_delete_cookie(command, token_key)

        session_id = self.cookies_manager.get_cookie(
            command.request, TokenKeyType.SESSION_ID_TOKEN.value
        )
        if session_id is None:
            logger.warning("No session ID found in the cookies.")
        else:
            logger.debug(f"Found session ID: {session_id}")
            await self._logout_user_from_all_sessions(session_id)
            await self._revoke_and_delete_cookie(
                command, TokenKeyType.SESSION_ID_TOKEN.value
            )

        response = Response(
            content={"message": "User logged out successfully"},
            media_type=MediaType.JSON,
            headers=command.response.headers,
            status_code=200,
        )
        return response

    async def _revoke_and_delete_cookie(
        self, command: LogoutCommand, token_key: str
    ):
        """Revoke a token and delete the associated cookie if it exists."""
        cookie = self.cookies_manager.get_cookie(command.request, token_key)
        logger.debug(f"Processing cookie for token: {token_key}")

        if cookie is not None:
            revoke_response = await self.revocation_service.revoke(token_key)
            logger.info(
                f"Token {token_key} revocation response: {revoke_response}"
            )
            self.cookies_manager.delete_cookie(command.response, token_key)
            logger.info(f"Deleted cookie for token: {token_key}")
        else:
            logger.debug(f"No cookie found for token: {token_key}")

    async def _logout_user_from_all_sessions(self, session_id: str):
        """Log the user out from all active sessions and clean up session data."""
        logger.info("Logout user from all sessions")

        try:
            logger.debug(
                f"Attempting to retrieve user session for session ID: {session_id}"
            )
            user_session_data = (
                await self.user_active_session_service.get_user_session(
                    session_id
                )
            )
            if user_session_data is None:
                logger.debug(
                    f"No active session data found for session ID: {session_id}"
                )
                return

            logger.debug(
                f"User session data retrieved successfully: {user_session_data}"
            )

            try:
                logger.debug(
                    f"Validating user session data for session ID: {session_id}"
                )
                user_session = UserSessionData.model_validate(
                    user_session_data
                )
                logger.debug(
                    f"User session data validated successfully: {user_session}"
                )
            except ValidationError as e:
                logger.error(f"Failed to validate user session data: {e}")
                return

            # Handle session cleanup
            logger.debug(
                f"Getting user sessions key for user ID: {user_session.user_id}"
            )
            user_sessions_key = self.session_key_manager.get_user_sessions_key(
                user_session.user_id
            )
            logger.debug(f"User sessions key retrieved: {user_sessions_key}")

            product_sessions_key = None
            if user_session.product_id:
                logger.debug(
                    f"Getting product sessions key for product ID: {user_session.product_id}"
                )
                product_sessions_key = (
                    self.session_key_manager.get_product_sessions_key(
                        user_session.product_id
                    )
                )
                logger.debug(
                    f"Product sessions key retrieved: {product_sessions_key}"
                )
            else:
                logger.debug(
                    "No product ID found for user session, skipping product sessions cleanup."
                )

            # Deleting user session
            logger.debug(
                f"Getting user sessions key for user ID: {user_session.user_id}"
            )
            user_sessions_key = self.session_key_manager.get_user_sessions_key(
                user_session.user_id
            )
            logger.debug(f"User sessions key retrieved: {user_sessions_key}")

            # Deleting user from user sessions
            logger.debug(
                f"Deleting user from user sessions with sessions key: {user_sessions_key}"
            )
            delete_user_from_user_sessions_response = await self.user_active_session_service.delete_user_session_from_user_sessions(
                session_id, user_sessions_key
            )
            logger.debug(
                f"User deletion from user sessions response: {delete_user_from_user_sessions_response}"
            )

            # Deleting empty user sessions
            logger.debug(
                f"Deleting empty user sessions for sessions key: {user_sessions_key}"
            )
            delete_empty_user_sessions_response = await self.user_active_session_service.delete_empty_user_sessions(
                user_sessions_key
            )
            logger.debug(
                f"Empty user sessions deletion response: {delete_empty_user_sessions_response}"
            )

            # Deleting user from product sessions if applicable
            if product_sessions_key:
                logger.debug(
                    f"Deleting user from product sessions with product sessions key: {product_sessions_key}"
                )
                delete_user_from_product_sessions_response = await self.user_active_session_service.delete_user_session_from_product_sessions(
                    session_id, product_sessions_key
                )
                logger.debug(
                    f"User deletion from product sessions response: {delete_user_from_product_sessions_response}"
                )

            # Deleting user from online sessions
            logger.debug(
                f"Deleting user session from online sessions with sessions key: {user_sessions_key}"
            )
            delete_online_user_response = await self.user_active_session_service.delete_user_session_from_online(
                user_sessions_key
            )
            logger.debug(
                f"User session deleted from online sessions: {delete_online_user_response}"
            )

        except Exception as e:
            logger.error(
                f"Error during session logout for session ID {session_id}: {e}"
            )
