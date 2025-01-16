from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)

from fastapi import Request, status
import httpx


class HttpxEequestErrorHandler(BaseErrorHandler[httpx.RequestError]):
    async def exception_handler(
        self, request: Request, exc: httpx.RequestError
    ):
        """."""
        raise WebServiceError(
            error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=exc,
            description="",
            error_class=httpx.RequestError,
            error_severity="CRITICAL_SHUTDOWN",
            error_category_type="INTERNAL_SERVICE_ERROR",
            message="MESSAGE ERROR",
            title="Internal Service HTTPX timeout exception",
            user_message="violates unique constraint",
        )
