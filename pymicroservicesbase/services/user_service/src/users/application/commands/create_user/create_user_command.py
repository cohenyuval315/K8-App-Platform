from typing import Annotated, List
from pydantic import Field
from fastapi import Body, Depends, Query

from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,BaseUserCommandDep
)
from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.create_user_schema import CreateUserSchema


class CreateUserCommand(BaseUserWebCommand):
    data: CreateUserSchema = Field(
        ..., description="Details for creating a user"
    )


async def get_create_user_command(
    base_user_command:BaseUserCommandDep,
    data: CreateUserSchema = Body(),

) -> CreateUserCommand:
    return CreateUserCommand(
        **base_user_command.model_dump(),
        data=data
    )


CreateUserCommandDep = Annotated[
    CreateUserCommand, Depends(get_create_user_command)
]
