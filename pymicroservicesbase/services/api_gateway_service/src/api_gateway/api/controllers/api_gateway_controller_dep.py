from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.api.controllers.api_gateway_controller import (
    APIGatewayController,
)
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.domain.services.api_gateway_service import (
    APIGatewayService,
)
from pymicroservicesbase.sdk.web_api.common.discovery.discovery import (
    ProductDiscoveryService,
    ServiceDiscoveryService,
)
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.domain.services.proxy_client import (
    ProxyClient,
)


def get_api_gateway_controller() -> APIGatewayController:
    return APIGatewayController(
        APIGatewayService(
            service_discovery_service=ServiceDiscoveryService(),
            product_discovery_service=ProductDiscoveryService(),
            proxy_client=ProxyClient(),
            authorization_service=None,
            authentication_service=None,
        )
    )


APIGatewayControllerDep = Annotated[
    APIGatewayController, Depends(get_api_gateway_controller)
]
