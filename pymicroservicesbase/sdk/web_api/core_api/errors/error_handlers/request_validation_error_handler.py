from collections import defaultdict
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
        error_message = await self.to_error_message(exc)
        raise WebServiceError(
            error_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_message=error_message,
            is_public=True,
        )

    async def format_error(self, exc: RequestValidationError):
        reformatted_message = defaultdict(list)
        for _error in exc.errors():
            loc, msg = _error["loc"], _error["msg"]
            filtered_loc = (
                loc[1:] if loc[0] in ("body", "query", "path") else loc
            )

            # field_string = ".".join([str(item) for item in filtered_loc])
            field_string = ".".join(filtered_loc)
            reformatted_message[field_string].append(msg)
        return reformatted_message

    async def to_error_message(self, exc: RequestValidationError) -> str:
        error_messages = await self.format_error(exc)
        error_message = []
        for field, msgs in error_messages.items():
            msg = f"{field} " + ",".join(msgs).lower()
            error_message.append(msg)
        error_message = ",".join(error_message)
        return error_message
