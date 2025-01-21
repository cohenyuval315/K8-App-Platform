# from apikit.src.middlewares.relational_db_middleware import RelationalDBMiddleware


from contextlib import asynccontextmanager

from pymicroservicesbase.sdk.web_api.common.db.sql.errors.set_sql_errors_handlers import (
    set_sql_db_errors_handlers,
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
from pymicroservicesbase.services.user_service.logger import logger
from pymicroservicesbase.services.user_service.src.config.config import config
from pymicroservicesbase.services.user_service.src.database.connection import (
    db,
)
from pymicroservicesbase.services.user_service.src.users.api.routes.user_router import (
    user_router,
)


@asynccontextmanager
async def lifespan(app: WebService):
    logger.info("starting app")
    res = await db.ping()
    async with db.with_connection() as conn:
        await conn.run_sync(db.metadata.drop_all)
        await conn.run_sync(db.metadata.create_all)
        await conn.commit()
    logger.info(res)
    try:
        yield
    finally:
        logger.info("on exit")


def create_user_web_service() -> WebServiceContainer:
    web_service_logger = WebServiceLogger(logger=logger)
    container = create_web_service_container(
        lifespan=lifespan,
        logger=web_service_logger,
        config=config,
        routers=[user_router],
    )
    web_service = container.get_web_service()
    set_sql_db_errors_handlers(web_service)

    return container
