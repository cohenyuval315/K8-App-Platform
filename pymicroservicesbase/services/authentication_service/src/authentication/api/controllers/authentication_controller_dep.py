from typing import Annotated
from fastapi import Depends, Request
from pymicroservicesbase.sdk.services.internal.internal_user_service_client import (
    InternalUserServiceClient,
)
from pymicroservicesbase.services.authentication_service.src.authentication.api.controllers.authentication_controller import (
    AuthenticationController,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.providers.auth_provider_service import (
    AuthProviderService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.authentication_service import (
    AuthenticationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.tokens_service import (
    TokenService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_active_session_service import (
    UserActiveSessionService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_session_service import (
    UserSessionService,
)
from pymicroservicesbase.services.authentication_service.src.cookies.cookies_manager import (
    CookiesManager,
)
from pymicroservicesbase.shared.constants.headers import (
    CONTENT_LENGTH_HEADER_KEY,
    HOST_HEADER_KEY,
)
from pymicroservicesbase.utils.tokens.jwt_token_factory import JWTConfig
from pymicroservicesbase.utils.tokens.token_factory import TokenFactory
from pymicroservicesbase.utils.tokens.token_type import TokenType
from pymicroservicesbase.sdk.cache.in_memory_async_cache import (
    InMemoryAsyncCache,
)

# cache = RedisAsyncCache("redis")
cache = InMemoryAsyncCache()


async def get_authentication_controller(
    request: Request,
) -> AuthenticationController:
    cookie_manager = CookiesManager(
        path="/", domain=None, samesite="none", secure=True, httponly=True
    )

    return AuthenticationController(
        AuthenticationService(
            user_service=InternalUserServiceClient()
            .without_headers(headers=[HOST_HEADER_KEY])
            .with_purged_headers(
                request.headers.items(),
                [
                    CONTENT_LENGTH_HEADER_KEY,
                    HOST_HEADER_KEY,
                ],
            )
            .with_cookies(request.cookies)
            .without_headers(headers=[CONTENT_LENGTH_HEADER_KEY]),
            user_session_service=UserSessionService(cache),
            user_active_session_service=UserActiveSessionService(cache),
            cookies_manager=cookie_manager,
            token_service=TokenService(
                token_factory=TokenFactory()
                .configure(
                    TokenType.JWT,
                    JWTConfig(
                        key="secret_key",
                        sort_headers=True,
                        algorithm="HS256",
                        require=["exp"],
                        algorithms=["HS256"],
                        leeway=10,
                        verify_signature=True,
                        verify_aud=True,
                        verify_iss=True,
                        verify_exp=True,
                        verify_iat=True,
                        verify_nbf=True,
                        strict_aud=True,
                    ),
                )
                .configure(TokenType.UUID, length=36)
            ),
            auth_provider_service=AuthProviderService(),
        )
    )


AuthenticationControllerDep = Annotated[
    AuthenticationController, Depends(get_authentication_controller)
]
