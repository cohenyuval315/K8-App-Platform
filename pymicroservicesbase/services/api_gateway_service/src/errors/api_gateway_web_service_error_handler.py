from fastapi import Request
from fastapi.responses import JSONResponse
from pymicroservicesbase.sdk.web_api.core_api.errors.base_error_handler import (
    BaseErrorHandler,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.api_gateway_service.logger import logger


class APIGatewayWebServiceErrorHandler(BaseErrorHandler[WebServiceError]):
    async def exception_handler(self, request: Request, exc: WebServiceError):
        status_code = (
            exc.error_code if isinstance(exc.error_code, int) else 500
        )
        logger.error(exc.as_dict())
        response = JSONResponse(
            status_code=status_code,
            content=WebServiceError.pack(exc.flatten_public_dict_bfs()),
        )
        logger.error(response)
        return response
