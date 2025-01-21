from typing import Annotated
from fastapi import Depends, Request
from pymicroservicesbase.sdk.services.internal.internal_user_service_client import (
    InternalUserServiceClient,
)
from pymicroservicesbase.services.authentication_service.src.authentication.api.controllers.authentication_controller import (
    AuthenticationController,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.identity_service.identity_service import (
    IdentityService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.login_service.login_service import (
    LoginService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.logout_service.logout_service import (
    LogoutService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.authentication_service import (
    AuthenticationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.refresh_service.refresh_service import (
    RefreshService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.revocation.revocation_service import (
    RevocationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.session_key_manager import (
    SessionKeyManager,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.signup_service.signup_service import (
    SignupService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.tokens_service import (
    TokenService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.sessions.user_active_session_service import (
    UserActiveSessionService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.verify_service.verify_service import (
    VerifyService,
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
session_key_manager = SessionKeyManager()

revocation_service = RevocationService(cache)

internal_service_access = {
    "client_id": "auth_client_id",
    "client_secret": "auth_client_id",
    "scope": "",
}


refresh_token_expire = 24 * 60 * 60
access_token_expire = 20 * 60
session_token_expire = 10 * 60
session_id_token_expire = 5 * 60
csrf_token_expire = 5 * 60
session_ttl = 5 * 60


async def get_authentication_controller(
    request: Request,
) -> AuthenticationController:
    cookies_manager = CookiesManager(
        path="/", domain=None, samesite="none", secure=True, httponly=True
    )
    user_service = (
        InternalUserServiceClient()
        .without_headers(headers=[HOST_HEADER_KEY])
        .with_purged_headers(
            request.headers.items(),
            [
                CONTENT_LENGTH_HEADER_KEY,
                HOST_HEADER_KEY,
            ],
        )
        .with_cookies(request.cookies)
        .without_headers(headers=[CONTENT_LENGTH_HEADER_KEY])
    )
    token_factory = (
        TokenFactory()
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
    )
    token_service = TokenService(token_factory=token_factory)
    user_active_session_service = UserActiveSessionService(cache)

    return AuthenticationController(
        AuthenticationService(
            login_service=LoginService(
                user_service=user_service,
                token_service=token_service,
                user_active_session_service=user_active_session_service,
                cookies_manager=cookies_manager,
                internal_service_access=internal_service_access,
                refresh_token_expire=refresh_token_expire,
                access_token_expire=access_token_expire,
                session_token_expire=session_token_expire,
                session_id_token_expire=session_id_token_expire,
                csrf_token_expire=csrf_token_expire,
                session_ttl=session_ttl,
            ),
            signup_service=SignupService(user_service),
            verify_service=VerifyService(
                cookies_manager=cookies_manager,
                user_active_session_service=user_active_session_service,
                token_service=token_service,
                refresh_token_expire=refresh_token_expire,
                access_token_expire=access_token_expire,
                session_token_expire=session_token_expire,
                session_id_token_expire=session_id_token_expire,
                csrf_token_expire=csrf_token_expire,
                session_ttl=session_ttl,
            ),
            logout_service=LogoutService(
                user_active_session_service=user_active_session_service,
                cookies_manager=cookies_manager,
                revocation_service=revocation_service,
                session_key_manager=session_key_manager,
            ),
            refresh_service=RefreshService(
                cookies_manager=cookies_manager,
                internal_service_access=internal_service_access,
                token_service=token_service,
                user_active_session_service=user_active_session_service,
                refresh_token_expire=refresh_token_expire,
                access_token_expire=access_token_expire,
                session_token_expire=session_token_expire,
                session_id_token_expire=session_id_token_expire,
                csrf_token_expire=csrf_token_expire,
                session_ttl=session_ttl,
            ),
            identity_service=IdentityService(),
        )
    )


AuthenticationControllerDep = Annotated[
    AuthenticationController, Depends(get_authentication_controller)
]
