from pydantic import EmailStr
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)

class PublicUserModel(BaseUserViewModel):
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
