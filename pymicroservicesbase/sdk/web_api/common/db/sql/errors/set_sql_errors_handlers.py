from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from .integrity_error_handler import IntegrityErrorHandler
from .sqlalchemy_error_handler import SQLalchemyErrorHandler
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def set_sql_db_errors_handlers(web_service: WebService):
    web_service.add_exception_handler(
        IntegrityError, IntegrityErrorHandler().exception_handler
    )
    web_service.add_exception_handler(
        SQLAlchemyError, SQLalchemyErrorHandler().exception_handler
    )
