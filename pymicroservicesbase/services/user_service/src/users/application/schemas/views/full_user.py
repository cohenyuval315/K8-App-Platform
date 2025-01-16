from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
)


class FullUserModel(BaseUserModel):
    id: str
    first_name: str | None
    username: str
