from typing import Annotated

from fastapi import Depends, Path
from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,
    BaseUserCommandDep,
)


class DeleteUserCommand(BaseUserWebCommand):
    user_id: str


async def get_delete_user_command(
    base_user_command: BaseUserCommandDep, user_id: str = Path(alias="user_id")
) -> DeleteUserCommand:
    _base_user_command = base_user_command.model_dump()
    merged_data = {**_base_user_command, "user_id": user_id}
    command = DeleteUserCommand(
        **merged_data,
    )
    return command


DeleteUserCommandDep = Annotated[
    DeleteUserCommand, Depends(get_delete_user_command)
]
