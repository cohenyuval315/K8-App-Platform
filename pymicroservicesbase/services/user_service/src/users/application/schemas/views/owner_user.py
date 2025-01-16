from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
)


class OwnerUserModel(BaseUserModel):
    first_name: str | None
    last_name: str | None
    username: str
