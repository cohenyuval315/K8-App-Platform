from starlette.datastructures import MutableHeaders


class ResponsePurgeHeadersMiddleware:
    def __init__(self, app, headers):
        self.app = app
        self.headers = headers

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def send_with_purge(message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                for header in self.headers:
                    if header in headers:
                        del headers[header]

            await send(message)

        await self.app(scope, receive, send_with_purge)
