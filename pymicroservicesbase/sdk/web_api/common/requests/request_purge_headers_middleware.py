from starlette.datastructures import MutableHeaders


class RequestPurgeHeadersMiddleware:
    def __init__(self, app, headers):
        self.app = app
        self.headers = headers

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request_headers = MutableHeaders(scope=scope)
        new_headers = MutableHeaders()
        for header, value in request_headers.items():
            if header not in self.headers:
                new_headers.append(header, value)

        scope["headers"] = new_headers.raw

        await self.app(scope, receive, send)
