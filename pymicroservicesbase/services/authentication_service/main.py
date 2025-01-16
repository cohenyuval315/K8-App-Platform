from pymicroservicesbase.services.authentication_service.src.app import (
    create_authentication_web_service,
)


service = create_authentication_web_service()
app = service.get_web_service()
