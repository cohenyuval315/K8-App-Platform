from fastapi import Request
from starlette.responses import Response

from pymicroservicesbase.services.api_gateway_service.logger import logger


class RequestPrivatePathMiddleware:
    def __init__(self, app, private_routes):
        self.app = app
        self.private_routes = private_routes

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope=scope, receive=receive)
        path = request.url.path

        for route in self.private_routes:
            if path.startswith(route):
                logger.warning(
                    f"someone tried to access private route: '{path}'"
                )
                response = Response(status_code=403)
                await response(scope, receive, send)
                return

        await self.app(scope, receive, send)
