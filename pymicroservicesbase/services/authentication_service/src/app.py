# from apikit.src.middlewares.relational_db_middleware import RelationalDBMiddleware
import logging
from contextlib import asynccontextmanager

from pymicroservicesbase.sdk.services.internal.internal_user_service_client import (
    InternalUserServiceClient,
)
from pymicroservicesbase.sdk.web_api.core_api.logging.web_service_logger import (
    WebServiceLogger,
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
from pymicroservicesbase.services.authentication_service.src.config.config import (
    config,
)
from pymicroservicesbase.services.authentication_service.src.middleware.csrf_token_middleware import (
    CSRFTokenMiddleware,
)
from pymicroservicesbase.shared.constants.headers import CSRF_TOKEN_HEADER_KEY
from pymicroservicesbase.shared.logging import create_logger
from pymicroservicesbase.utils.tokens.token_key_type import TokenKeyType


@asynccontextmanager
async def lifespan(app: WebService):
    user_service = InternalUserServiceClient()

    yield

    await user_service.close()


def create_authentication_web_service() -> WebServiceContainer:
    logger = create_logger(
        level=logging.DEBUG,
        loggers_levels={
            "uvicorn": {
                "handlers": ["default", "file_handler"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["stream_handler", "file_handler"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["stream_handler", "file_handler"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            "uvicorn.asgi": {
                "handlers": ["stream_handler", "file_handler"],
                "level": logging.DEBUG,
                "propagate": False,
            },
        },
    )
    web_service_logger = WebServiceLogger(logger=logger)

    container = create_web_service_container(
        lifespan=lifespan,
        logger=web_service_logger,
        config=config,
        routers=[authentication_router],
    )
    web_service = container.get_web_service()
    web_service.add_middleware(
        CSRFTokenMiddleware,
        TokenKeyType.CSRF_TOKEN.value,
        CSRF_TOKEN_HEADER_KEY,
        ["auth/refresh"],  # exclude
    )

    return container
