from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from fastapi import Request, status

# if TYPE_CHECKING:
from sqlalchemy.exc import OperationalError


class OperationalErrorHandler(BaseErrorHandler[OperationalError]):
    async def exception_handler(self, request: Request, exc: OperationalError):
        """Handle OperationalError exception."""

        raise WebServiceError(
            error_code=status.HTTP_409_CONFLICT,
            error=exc,
            description="database error",
            error_severity="NONE_OPERATIONAL",
            error_category_type="DATABASE_ERROR",
            user_message="violates unique constraint",
        )
