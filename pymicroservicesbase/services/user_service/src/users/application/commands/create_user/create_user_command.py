from typing import Annotated, List
from pydantic import Field
from fastapi import Body, Depends

from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,
    BaseUserCommandDep,
)

from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.create_user_options import (
    CreateUserOptions,
)


class CreateUserCommand(BaseUserWebCommand):
    data: CreateUserOptions = Field(
        ..., description="Details for creating a user"
    )


async def get_create_user_command(
    base_user_command: BaseUserCommandDep, data: CreateUserOptions = Body(...)
) -> CreateUserCommand:
    _base_user_command = base_user_command.model_dump()
    _data = data.model_dump()
    merged_data = {**_base_user_command, "data": {**_data}}
    command = CreateUserCommand(
        **merged_data,
    )
    return command


async def get_create_user_options():
    return []


CreateUserOptionsDep = Annotated[
    List[CreateUserOptions], Depends(get_create_user_options)
]

CreateUserCommandDep = Annotated[
    CreateUserCommand, Depends(get_create_user_command)
]
