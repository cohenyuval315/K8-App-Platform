from typing import Annotated

from fastapi import Depends, Path, Body
from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,
    BaseUserCommandDep,
)


class UpdateUserData(BaseModel):
    first_name: str
    last_name: str


class UpdateUserCommand(BaseUserWebCommand):
    user_id: str
    attributes: UpdateUserData = Field(
        ..., description="Details for creating a user"
    )


async def get_update_user_command(
    base_user_command: BaseUserCommandDep,
    data: UpdateUserData = Body(...),
    user_id: str = Path(alias="user_id"),
) -> UpdateUserCommand:
    _base_user_command = base_user_command.model_dump()
    _data = data.model_dump()
    merged_data = {
        **_base_user_command,
        "attributes": {**_data},
        "user_id": user_id,
    }
    command = UpdateUserCommand(
        **merged_data,
    )
    return command


UpdateUserCommandDep = Annotated[
    UpdateUserCommand, Depends(get_update_user_command)
]
