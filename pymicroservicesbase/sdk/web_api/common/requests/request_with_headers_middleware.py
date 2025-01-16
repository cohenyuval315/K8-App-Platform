from starlette.datastructures import MutableHeaders


class RequestWithHeadersMiddleware:
    def __init__(self, app, headers):
        self.app = app
        self.headers = headers

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        headers = MutableHeaders(scope=scope)
        for header, value in self.headers:
            headers.append(header, value)

        scope["headers"] = headers.raw

        await self.app(scope, receive, send)
