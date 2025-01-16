from typing import Any, List, Sequence, Tuple, Union

from fastapi import Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_errors import (
    WebServiceErrors,
)
from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)
from pymicroservicesbase.shared.logging import logger


class CentralErrorHandler:
    """Error Handler

    Raises:
        RuntimeError:

    Returns:
        Response
    """

    @staticmethod
    async def handle_request_error(
        request: Request, web_service_error: Exception
    ) -> JSONResponse:
        logger.error(web_service_error)
        return await CentralErrorHandler.handle_error(web_service_error)

    @staticmethod
    def normalize_error_messages(
        error_messages: Union[str, Sequence, None],
    ) -> Sequence[str] | str | None:
        if error_messages is None:
            return None
        elif isinstance(error_messages, str):
            return error_messages  # Already valid
        elif isinstance(error_messages, Sequence):
            # Flatten the sequence if it contains nested structures
            flattened = []
            for item in error_messages:
                if isinstance(item, dict):
                    flattened.append(str(item))  # Convert dict to string
                elif isinstance(item, str):
                    flattened.append(item)
                else:
                    flattened.append(
                        repr(item)
                    )  # Generic string representation
            return (
                flattened if len(flattened) > 1 else flattened[0]
            )  # Keep as str if single item
        else:
            # Convert unexpected types to a string
            return str(error_messages)

    @staticmethod
    async def handle_error(web_service_error: Exception) -> JSONResponse:
        """_summary_

        Args:
            request (Request): _description_
            web_service_error (Exception): _description_

        Returns:
            BaseResponseSchemaSchema: _description_
        """
        status_code, error_messages = CentralErrorHandler._get_error_response(
            web_service_error
        )

        if isinstance(status_code, int):
            _status_code = status_code
        else:
            _status_code = 500

        response = BaseResponseSchema(
            errors=CentralErrorHandler.extract_error_messages(error_messages),
        )

        return JSONResponse(
            status_code=_status_code, content=response.model_dump()
        )

    @staticmethod
    def _get_error_response(
        web_service_error: Exception,
    ) -> Tuple[int | str, str | Sequence[str] | Sequence[Any] | None]:
        """
        Determines the status code and error message based on the exception type.
        Each error type is mapped to an appropriate HTTP status code and message.
        """

        if isinstance(web_service_error, WebServiceError):
            _status = (
                web_service_error.error_code
                if web_service_error.error_code is not None
                else status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            _msg = (
                web_service_error.user_message
                if web_service_error.user_message
                else None
            )
            return _status, _msg

        elif isinstance(web_service_error, HTTPException):
            return web_service_error.status_code, web_service_error.detail

        elif isinstance(web_service_error, StarletteHTTPException):
            return status.HTTP_400_BAD_REQUEST, web_service_error.detail

        elif isinstance(web_service_error, RequestValidationError):
            return status.HTTP_400_BAD_REQUEST, web_service_error.errors()

        elif isinstance(web_service_error, ValidationError):
            return status.HTTP_400_BAD_REQUEST, web_service_error.errors()

        elif (
            isinstance(web_service_error, WebServiceErrors)
            or issubclass(web_service_error.__class__, Exception)
            or isinstance(web_service_error, Exception)
        ):
            return (
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "An unexpected error occurred.",
            )

        return (
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "An unexpected error occurred.",
        )

    @staticmethod
    def format_error_details(error: dict, error_type: str) -> str:
        """
        Helper function to format the error message based on the type of error.
        """
        loc = error.get("loc", [])
        field = loc[-1] if loc else "unknown"
        current_value = error.get("input", "unknown value")

        # Common base error message
        base_message = f'Error in field "{field}": '

        if error_type == "missing":
            return base_message + "The required field is missing in the path."

        if error_type == "invalid":
            return (
                base_message
                + f'The field "{field}" is invalid. It should be a different type. Current value: {current_value}.'
            )

        if error_type == "type_error":
            expected_type = error.get("expected", "unknown type")
            return (
                base_message
                + f'The field "{field}" has a type error. Expected type: {expected_type}, but got {type(current_value).__name__}. Current value: {current_value}.'
            )

        if error_type == "value_error":
            error_message = error.get("msg", "Invalid value")
            return (
                base_message
                + f'The field "{field}" has an invalid value. {error_message}.'
            )

        if error_type == "field_error":
            return base_message + error.get("msg", "Unknown field error.")

        # Default for unexpected error types
        return (
            base_message
            + f"Unexpected error: {error.get('msg', 'Unknown error')}."
        )

    @staticmethod
    def format_error_message(error: dict) -> str:
        """
        Main function to identify the error type and delegate formatting.
        """
        error_type = error.get("type", "unknown")
        return CentralErrorHandler.format_error_details(error, error_type)

    @staticmethod
    def extract_error_messages(errors: Any) -> Union[str, List[str]]:
        if isinstance(errors, dict):
            # Format a single error message
            return CentralErrorHandler.format_error_message(errors)
        elif isinstance(errors, list):
            # Process each error in the list and format them
            return [
                CentralErrorHandler.format_error_message(error)
                for error in errors
            ]
        else:
            # If it's a single string or unexpected format, just return it
            return str(errors)
