from pymicroservicesbase.services.api_gateway_service.src.app import (
    create_api_gateway_web_service,
)


web_service_container = create_api_gateway_web_service()
app = web_service_container.get_web_service()
