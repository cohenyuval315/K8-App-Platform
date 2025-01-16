from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)


class RequestValidationErrorHandler(BaseErrorHandler[RequestValidationError]):
    async def exception_handler(
        self, request: Request, exc: RequestValidationError
    ):
        """Handle TimeoutException exception."""
        raise WebServiceError(
            error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=exc,
            description="",
            error_class=RequestValidationError,
            error_severity="CRITICAL_SHUTDOWN",
            error_category_type="INTERNAL_SERVICE_ERROR",
            message="MESSAGE ERROR",
            title="Internal Service HTTPX timeout exception",
            user_message="violates unique constraint",
        )
