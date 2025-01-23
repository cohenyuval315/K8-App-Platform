from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)

class FullUserModel(BaseUserViewModel):
    id: str
    first_name: str | None
    username: str
