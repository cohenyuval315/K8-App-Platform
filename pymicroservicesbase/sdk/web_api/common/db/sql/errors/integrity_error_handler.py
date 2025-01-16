from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from fastapi import Request, status
import re

# if TYPE_CHECKING:
from sqlalchemy.exc import IntegrityError


class IntegrityErrorHandler(BaseErrorHandler[IntegrityError]):
    def __init__(self):
        super().__init__(IntegrityError)
        self.unique_constraint_error_messages = [
            "UNIQUE constraint failed",  # SQLite
            "Duplicate entry",  # MySQL
            "violates unique constraint",  # PostgreSQL
        ]

    async def exception_handler(self, request: Request, exc: IntegrityError):
        """Handle IntegrityError exception."""
        exc_orig_str = str(exc.orig)
        if any(
            error_msg in exc_orig_str
            for error_msg in self.unique_constraint_error_messages
        ):
            # get_message()
            error_message = self.normalize_error_message(exc._message())
            raise WebServiceError(
                error_code=status.HTTP_409_CONFLICT,
                error_message=error_message,
                is_public=True,
            )

    def normalize_error_message(self, error_message: str) -> str:
        # Regular expression to capture any key and its value
        pattern = r"Key \((.*?)\)=\((.*?)\) already exists"

        # Search for the pattern in the error message
        match = re.search(pattern, error_message)

        if match:
            # If a match is found, extract the key and value
            key = match.group(1)
            value = match.group(2)
            # Format the message
            return f"{key.capitalize()} '{value}' Already Exists"

        return "Already Exists"
