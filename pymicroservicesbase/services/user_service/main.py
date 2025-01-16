from pymicroservicesbase.services.user_service.src.app import (
    create_user_web_service,
)

web_service_container = create_user_web_service()
app = web_service_container.get_web_service()
