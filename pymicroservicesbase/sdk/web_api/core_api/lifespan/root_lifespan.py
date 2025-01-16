from contextlib import AsyncExitStack, asynccontextmanager

from starlette.routing import Mount

from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService


@asynccontextmanager
async def root_lifespan(app: WebService):
    async with (
        AsyncExitStack() as stack
    ):  # handle multiple async context manager
        for route in app.routes:
            if isinstance(route, Mount) and isinstance(route.app, WebService):
                await stack.enter_async_context(
                    route.app.router.lifespan_context(
                        route.app
                    ),  # all lifespans for all subapps
                )
        yield


def _lifespan(lifespan):
    @asynccontextmanager
    async def lifespan_context(app: WebService):
        async with root_lifespan(app):
            async with lifespan(app):
                yield

    return lifespan_context
