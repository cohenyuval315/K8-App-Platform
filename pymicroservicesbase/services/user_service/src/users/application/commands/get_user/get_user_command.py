from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,BaseUserCommandDep
)
from fastapi import Path, Depends
from typing import Annotated


class GetUserCommand(BaseUserWebCommand):
    user_id: str


async def get_get_user_command(
    base_user_command:BaseUserCommandDep,
    user_id: str = Path(alias="user_id")
) -> GetUserCommand:
    return GetUserCommand(
        **base_user_command.model_dump(),
        user_id=user_id
    )


GetUserCommandDep = Annotated[GetUserCommand, Depends(get_get_user_command)]
