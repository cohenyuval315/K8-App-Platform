import time

from starlette.datastructures import MutableHeaders

from pymicroservicesbase.shared.constants.headers import (
    RESPONSE_TIME_HEADER_KEY,
)


class ResponseTimeMiddleware:
    def __init__(self, app):
        self.app = app
        self.header_key = RESPONSE_TIME_HEADER_KEY

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        start_time = time.time()

        async def send_with_extra_headers(message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                elapsed_duration = time.time() - start_time
                elapsed_ms = f"{elapsed_duration * 1000:.2f}ms"  # Convert to milliseconds
                headers.append(self.header_key, elapsed_ms)

            await send(message)

        await self.app(scope, receive, send_with_extra_headers)
