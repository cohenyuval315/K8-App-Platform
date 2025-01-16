from typing import Any

from fastapi import Response
from fastapi.responses import JSONResponse

from pymicroservicesbase.sdk.web_api.common.discovery.discovery import (
    ProductDiscoveryService,
    ServiceDiscoveryService,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.api_gateway_service.logger import logger
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.domain.services.proxy_client import (
    ProxyClient,
)
from pymicroservicesbase.services.api_gateway_service.src.application.commands.api_request.api_request_command import (
    ApiRequestCommand,
)


class APIGatewayService:
    def __init__(
        self,
        service_discovery_service: ServiceDiscoveryService,
        product_discovery_service: ProductDiscoveryService,
        proxy_client: ProxyClient,
        authorization_service: Any,
        authentication_service: Any,
    ):
        self.proxy_client = proxy_client
        self.service_discovery_service = service_discovery_service
        self.product_discovery_service = product_discovery_service
        self.authentication_service = authentication_service
        self.authorization_service = authorization_service

    async def proxy_request(self, command: ApiRequestCommand):
        logger.info(
            f"Forwarding request to service URL: {command.service_url}"
        )
        _response = await self.proxy_client.forward_request(
            url=command.service_url,
            method=command.request.method,
            request=command.request,
        )
        if _response.is_error:
            res = _response.json()
            result = dict(res)
            error_tree = WebServiceError.unpack(result)
            logger.critical(error_tree)
            flat_error_tree = WebServiceError.flatten(error_tree)
            content = WebServiceError.pack(flat_error_tree)
            logger.critical(content)
            return JSONResponse(
                status_code=_response.status_code,
                content=content,
                headers=_response.headers,
            )

        response = Response(
            status_code=_response.status_code,
            content=_response.content,
            headers=_response.headers,
        )
        return response
