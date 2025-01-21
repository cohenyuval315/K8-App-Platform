from typing import Callable, Dict, List

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from pymicroservicesbase.sdk.web_api.common.admin.api.routes.admin_router import (
    admin_router,
)
from pymicroservicesbase.sdk.web_api.common.configuration.api.routes.configuration_router import (
    configuration_router,
)
from pymicroservicesbase.sdk.web_api.common.debugging.api.routes.debugging_router import (
    debugging_router,
)
from pymicroservicesbase.sdk.web_api.common.health_check.api.routes.health_check_router import (
    health_check_router,
)
from pymicroservicesbase.sdk.web_api.common.logging.api.routes.logging_router import (
    logging_router,
)
from pymicroservicesbase.sdk.web_api.common.memory.api.routes.memory_router import (
    memory_router,
)
from pymicroservicesbase.sdk.web_api.common.profiling.api.routes.profiling_router import (
    profiling_router,
)

from pymicroservicesbase.sdk.web_api.common.responses.forward_headers_middleware import (
    ForwardHeadersMiddleware,
)
from pymicroservicesbase.sdk.web_api.common.status.api.routes.status_router import (
    status_router,
)
from pymicroservicesbase.sdk.web_api.core_api.configuration.base_web_service_config import (
    BaseWebServiceConfig,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.error_middleware import (
    ErrorMiddleware,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.set_error_handlers import (
    set_errors_handlers,
)

from pymicroservicesbase.sdk.web_api.core_api.logging.logging_middleware import (
    LoggingMiddleware,
)
from pymicroservicesbase.sdk.web_api.core_api.requests.request_id.request_id_middleware import (
    RequestIdContextMiddleware,
)

# from pymicroservicesbase.sdk.web_api.core_api.responses.response_middleware import (
#     ResponseMiddleware,
# )
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)
from pymicroservicesbase.sdk.web_api.variants.base_web_service import (
    create_base_web_service_container,
)
from pymicroservicesbase.sdk.web_api.web_context import WebContext
from pymicroservicesbase.shared.constants.headers import (
    CORRELATION_ID_HEADER_KEY,
)
from pymicroservicesbase.shared.logging import get_logger


def create_web_service_container(
    config: BaseWebServiceConfig,
    lifespan,
    routers: List[WebRouter] | None = None,
    health_checks: Dict[str, Callable] | None = {},
    with_web_service_error: bool = True,
    *args,
    **kwargs,
) -> WebServiceContainer:
    wsc = create_base_web_service_container(config, lifespan)
    web_service = wsc.get_web_service()
    logger = get_logger()

    # Routes
    root_router = WebRouter()
    root_router.include_router(admin_router)
    root_router.include_router(status_router)

    admin_router.include_router(debugging_router)
    admin_router.include_router(logging_router)
    admin_router.include_router(memory_router)
    admin_router.include_router(profiling_router)

    admin_router.include_router(health_check_router)
    admin_router.include_router(configuration_router)

    if routers is None:
        routers = []

    for router in routers:
        root_router.include_router(router)

    web_service.include_router(root_router)
    web_service.include_router(admin_router)

    web_service.add_middleware(ErrorMiddleware)
    web_service.add_middleware(LoggingMiddleware, logger)
    web_service.add_middleware(RequestIdContextMiddleware)
    web_service.add_middleware(SessionMiddleware, "secret")

    web_service.add_middleware(
        CORSMiddleware,
        allow_origins=config.system_config.ALLOW_ORIGINS,
        allow_credentials=config.system_config.ALLOW_CREDS,
        allow_methods=config.system_config.ALLOW_METHODS,
        allow_headers=config.system_config.ALLOW_HEADERS,
    )

    web_service.add_middleware(
        TrustedHostMiddleware, allowed_hosts=config.system_config.ALLOWED_HOSTS
    )

    web_service.add_middleware(
        GZipMiddleware,
        minimum_size=1024,  # # Compress responses greater than 1kB with optimal compression level as 5 # # with level ranging from 1 to 9 with 1 (fastest, least compression) # # and 9 (slowest, most compression)
        compresslevel=5,  # 1 -9 more compression = slower
    )
    web_service.add_middleware(
        ForwardHeadersMiddleware, [CORRELATION_ID_HEADER_KEY]
    )

    # web_service.add_middleware(ResponseMiddleware)

    if config.runtime_config.ENVIRONMENT == "production":
        web_service.add_middleware(HTTPSRedirectMiddleware)

    set_errors_handlers(web_service, with_web_service_error, logger=logger)

    WebContext.set_web_context(wsc)
    return wsc
