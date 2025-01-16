from fastapi import Request
from fastapi.responses import JSONResponse
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)


class WebServiceErrorHandler(BaseErrorHandler[WebServiceError]):
    def __init__(
        self, exception_cls=None, source: str | None = None, **kwargs
    ):
        super().__init__(exception_cls, **kwargs)
        self.source = source

    async def exception_handler(
        self, request: Request, exc: WebServiceError
    ) -> JSONResponse:
        status_code = (
            exc.error_code if isinstance(exc.error_code, int) else 500
        )
        response = JSONResponse(
            status_code=status_code, content=exc.pack([exc.as_dict()])
        )

        return response
