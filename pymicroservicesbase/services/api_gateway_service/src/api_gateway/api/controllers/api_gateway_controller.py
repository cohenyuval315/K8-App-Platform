from pymicroservicesbase.services.api_gateway_service.src.api_gateway.domain.services.api_gateway_service import (
    APIGatewayService,
)
from pymicroservicesbase.services.api_gateway_service.src.application.commands.api_request.api_request_command import (
    ApiRequestCommand,
)


class APIGatewayController:
    def __init__(self, api_gateway_service: APIGatewayService):
        self.api_gateway_service = api_gateway_service

    async def proxy_request(self, command: ApiRequestCommand):
        return await self.api_gateway_service.proxy_request(command)
