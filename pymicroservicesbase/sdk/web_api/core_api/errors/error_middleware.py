from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from starlette.types import ASGIApp, Scope, Receive, Send


class ErrorMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        try:
            if scope["type"] != "http":
                await self.app(scope, receive, send)
                return

            await self.app(scope, receive, send)
            return
        except Exception as e:
            raise WebServiceError(
                error_code=500,
                error_message=str(e),
                is_public=False,
                include_trace_errors=True,
            )
