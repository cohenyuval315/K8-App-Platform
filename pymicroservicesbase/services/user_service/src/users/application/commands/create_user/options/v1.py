from pydantic import EmailStr
from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.base_create_user_schema import (
    BaseCreateUserSchema,
)


class CreateUserVersionOne(BaseCreateUserSchema):
    username: str
    password: str
    email: EmailStr
