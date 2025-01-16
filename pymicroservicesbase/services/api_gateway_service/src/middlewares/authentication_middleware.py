from fastapi import Request, Response
from starlette.datastructures import MutableHeaders

from pymicroservicesbase.sdk.services.internal.internal_authentication_service import (
    InternalAuthenticationServiceClient,
)


class AuthenticationMiddleware:
    def __init__(
        self,
        app,
        authentication_client: InternalAuthenticationServiceClient,
        exclude_paths=None,
        include_paths=None,
    ):
        self.app = app
        self.authentication_client = authentication_client
        self.exclude_paths = (
            exclude_paths or []
        )  # Defaults to an empty list if not provided
        self.include_paths = include_paths or []

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        request = Request(scope, receive)
        path = request.url.path

        if any(
            path.startswith(excluded_path)
            for excluded_path in self.exclude_paths
        ) or not any(
            path.startswith(included_path)
            for included_path in self.include_paths
        ):
            await self.app(scope, receive, send)
            return

        auth_response = await self.authentication_client.verify(
            request.headers, request.cookies
        )

        if auth_response.status_code != 200:
            # result = auth_response.json()
            response = Response(status_code=401)
            await response(scope, receive, send)
            return

        async def send_with_headers(message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                for key, value in auth_response.headers:
                    headers.append(key, value)

            await send(message)

        await self.app(scope, receive, send_with_headers)
