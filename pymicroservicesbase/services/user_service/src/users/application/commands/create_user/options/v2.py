from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.base_create_user_schema import (
    BaseCreateUserSchema,
)


class CreateUserVersionTwo(BaseCreateUserSchema):
    username: str
    password: str
