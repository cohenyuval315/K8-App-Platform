from pydantic import Field
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)

class MinimalUserModel(BaseUserViewModel):
    id: str
    first_name: str | None
    last_name: str | None
    username: str
    password: str = Field(alias="hashed_password")
