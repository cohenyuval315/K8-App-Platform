from pydantic import EmailStr
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
)


class PublicUserModel(BaseUserModel):
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
