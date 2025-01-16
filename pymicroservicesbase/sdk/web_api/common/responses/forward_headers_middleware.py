from starlette.datastructures import MutableHeaders

from pymicroservicesbase.shared.logging import logger

# from starlette.requests import Request


class ForwardHeadersMiddleware:
    def __init__(self, app, headers):
        self.app = app
        self.headers = headers

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        forwarded_headers = MutableHeaders()
        headers = MutableHeaders(scope=scope)
        for header, value in headers.items():
            if header in self.headers:
                forwarded_headers.append(header, value)

                logger.debug(f"REQUEST FORWARD HEADERS: {forwarded_headers}")

        async def send_with_forwarded_headers(message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                for key, value in forwarded_headers.items():
                    headers.append(key, value)

                logger.debug(f"RESPONSE FORWARD HEADERS: {forwarded_headers}")

            await send(message)

        await self.app(scope, receive, send_with_forwarded_headers)
