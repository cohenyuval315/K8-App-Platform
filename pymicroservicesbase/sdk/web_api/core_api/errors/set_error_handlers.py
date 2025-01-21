from __future__ import annotations

from fastapi.exceptions import RequestValidationError


from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error_handler import (
    WebServiceErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.error_handlers.request_validation_error_handler import (
    RequestValidationErrorHandler,
)


def set_errors_handlers(
    web_service: WebService, with_web_service_error: bool = True, logger=None
):
    if with_web_service_error:
        web_service.add_exception_handler(
            WebServiceError,
            WebServiceErrorHandler(source=web_service.title).exception_handler,  # type: ignore
        )
    web_service.add_exception_handler(
        RequestValidationError,
        RequestValidationErrorHandler().exception_handler,
    )
    # web_service.add_exception_handler(
    #     ValidationError, ValidationErrorHandler().exception_handler
    # )
    # web_service.add_exception_handler(
    #     HTTPException, HTTPExceptionErrorHandler().exception_handler
    # )
    # web_service.add_exception_handler(
    #     StarletteHTTPException, StarletteHTTPExceptionErrorHandler().exception_handler
    # )
    # web_service.add_exception_handler(
    #     httpx.RequestError, HttpxEequestErrorHandler().exception_handler
    # )
    # web_service.add_exception_handler(
    #     Exception, ExceptionErrorHandler().exception_handler
    # )
