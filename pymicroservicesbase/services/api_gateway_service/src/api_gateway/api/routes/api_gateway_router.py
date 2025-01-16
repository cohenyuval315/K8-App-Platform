from fastapi import Response

from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.api.controllers.api_gateway_controller_dep import (
    APIGatewayControllerDep,
)
from pymicroservicesbase.services.api_gateway_service.src.application.commands.api_request.api_request_command import (
    ApiRequestCommandDep,
)

api_gateway_router = WebRouter(
    # prefix="/",
    tags=["api"],
)


@api_gateway_router.api_route(
    "/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    name="API Gateway Main Routing Function",
    description="This function acts as the main routing handler for the API gateway, forwarding requests to corresponding services. It handles various HTTP methods and allows for flexible service communication by proxying requests through the gateway.",
    summary="Routes incoming HTTP requests to the appropriate service through the API gateway, handling different HTTP methods such as GET, POST, PUT, DELETE, and PATCH.",
    tags=[
        "API Gateway",
        "Request Proxying",
        "HTTP Methods",
        "Service Routing",
        "Proxy",
        "Backend Communication",
    ],
)
async def proxy_request(
    api_gateway_controller: APIGatewayControllerDep,
    command: ApiRequestCommandDep,
) -> Response:
    return await api_gateway_controller.proxy_request(command)
