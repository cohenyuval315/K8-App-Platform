from typing import Annotated
from fastapi import Depends, Query
from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,BaseUserCommandDep
)

# from pymicroservicesbase.sdk.web_api.common.schemas.get_many_schema import GetManySchema
from pymicroservicesbase.sdk.web_api.common.params.query_params import (
    QueryParamsDep,
    QueryParams,
)


class GetManyUsersCommand(BaseUserWebCommand):
    query_params: QueryParams


async def get_get_many_users_command(
    base_user_command:BaseUserCommandDep,
    query_params:QueryParamsDep
) -> GetManyUsersCommand:
    return GetManyUsersCommand(
        **base_user_command.model_dump(),
        query_params=query_params
    )


GetManyUsersCommandDep = Annotated[
    GetManyUsersCommand, Depends(get_get_many_users_command)
]
