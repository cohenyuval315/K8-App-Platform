from fastapi import Request, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)


class StarletteHTTPExceptionErrorHandler(
    BaseErrorHandler[StarletteHTTPException]
):
    async def exception_handler(
        self, request: Request, exc: StarletteHTTPException
    ):
        """Handle TimeoutException exception."""
        raise WebServiceError(
            error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=exc,
            description="",
            error_class=StarletteHTTPException,
            error_severity="CRITICAL_SHUTDOWN",
            error_category_type="INTERNAL_SERVICE_ERROR",
            message="MESSAGE ERROR",
            title="Internal Service HTTPX timeout exception",
            user_message="violates unique constraint",
        )
