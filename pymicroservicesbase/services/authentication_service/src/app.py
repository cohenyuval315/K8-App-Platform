# from apikit.src.middlewares.relational_db_middleware import RelationalDBMiddleware
from contextlib import asynccontextmanager

from pymicroservicesbase.sdk.cache.in_memory_async_cache import (
    InMemoryAsyncCache,
)
from pymicroservicesbase.sdk.services.internal.internal_user_service_client import (
    InternalUserServiceClient,
)
from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)
from pymicroservicesbase.sdk.web_api.variants.full_web_service import (
    create_web_service_container,
)
from pymicroservicesbase.services.authentication_service.src.authentication.api.routes.authentication_router import (
    authentication_router,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.revocation.revocation_service import (
    RevocationService,
)
from pymicroservicesbase.services.authentication_service.src.config.config import (
    config,
)
from pymicroservicesbase.services.authentication_service.src.middleware.csrf_token_middleware import (
    CSRFTokenMiddleware,
)
from pymicroservicesbase.shared.constants.headers import CSRF_TOKEN_HEADER_KEY
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType


@asynccontextmanager
async def lifespan(app: WebService):
    user_service = InternalUserServiceClient()
    cache = InMemoryAsyncCache()
    revocation_service = RevocationService(cache)
    await cache.connect()
    await revocation_service.on_startup()
    yield
    await revocation_service.on_shutdown()
    await cache.close()
    await user_service.close()


def create_authentication_web_service() -> WebServiceContainer:

    container = create_web_service_container(
        lifespan=lifespan,
        config=config,
        routers=[authentication_router],
    )
    web_service = container.get_web_service()
    web_service.add_middleware(
        CSRFTokenMiddleware,
        TokenKeyType.CSRF_TOKEN.value,
        CSRF_TOKEN_HEADER_KEY,
        [  # exclude
            "auth/refresh",
            "/docs",
            "/openapi.json",
            "",
            "auth/verify",
        ],
    )

    return container
