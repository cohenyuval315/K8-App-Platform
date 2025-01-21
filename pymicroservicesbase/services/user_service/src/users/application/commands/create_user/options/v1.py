from pydantic import EmailStr, Field
from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.base_create_user_schema import (
    BaseCreateUserSchema,
)


class CreateUserVersionOne(BaseCreateUserSchema):
    username: str = Field(..., min_length=4, title="username")
    password: str = Field(..., min_length=4, title="password")
    email: EmailStr
