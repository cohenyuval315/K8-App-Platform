from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from fastapi import Request, status
from sqlalchemy.exc import SQLAlchemyError


class SQLalchemyErrorHandler(BaseErrorHandler[SQLAlchemyError]):
    def __init__(self):
        super().__init__(SQLAlchemyError)

    async def exception_handler(self, request: Request, exc: SQLAlchemyError):
        """Handle SQLALchemyErrpr exception."""
        raise WebServiceError(
            error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=exc,
            description="database error",
            error_class=SQLAlchemyError,
            error_severity="MEDIUM_LIMITED",
            error_category_type="DATABASE_ERROR",
            message=f"MESSAGE ERROR: {self.exception_cls._message} \n ,SQL ERROR: {self.exception_cls._sql_message}",
            title=f"SQLALCHEMY ERROR CODE: {self.exception_cls.code}, ",
        )
