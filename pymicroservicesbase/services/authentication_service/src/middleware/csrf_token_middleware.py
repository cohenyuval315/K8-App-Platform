from typing import List
from fastapi import Request

from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.api_gateway_service.logger import logger


class CSRFTokenMiddleware:
    def __init__(
        self,
        app,
        csrf_cookie_key: str,
        csrf_token_header_key: str,
        excluded_paths: List[str] | None = None,
    ):
        self.app = app
        if excluded_paths is None:
            excluded_paths = []
        self.excluded_paths = excluded_paths
        self.csrf_cookie_key = csrf_cookie_key
        self.csrf_token_header_key = csrf_token_header_key

    async def __call__(self, scope, receive, send):
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        request = Request(scope)
        request_path = request.url.path
        for path in self.excluded_paths:
            if request_path.startswith(path):
                await self.app(scope, receive, send)
                return

        csrf_token_cookie = request.cookies.get(self.csrf_cookie_key, None)
        if csrf_token_cookie is None:
            raise WebServiceError(
                error_code=400, error_message="CSRF Token Cookie Is Missing"
            )

        csrf_token = request.headers.get(self.csrf_token_header_key, None)
        if csrf_token is None:
            raise WebServiceError(
                error_code=400, error_message="CSRF Token Header Is Missing"
            )

        if csrf_token != csrf_token_cookie:
            logger.warning("CSRF tokens do not match, might be malicious...")
            raise WebServiceError(
                error_message=f"CSRF tokens do not match. Header CSRF token: {csrf_token}, Cookie CSRF token: {csrf_token_cookie}",
                error_code=401,
            )
            # TODO blacklist ip

        await self.app(scope, receive, send)
