from typing import Annotated, List
from fastapi import Query, Depends
from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.user_views import (
    UserViewType,
)


class BaseUserWebCommand(BaseWebCommand):
    view_type: UserViewType = Field(
        title="view_type", description="Defines the view type for the user"
    )


async def get_base_user_views(
    # config = None TODO
) -> List[UserViewType]:
    return ["minimal", "admin", "full", "internal", "owner", "public"]


async def get_base_user_command(
    views: List[UserViewType] = Depends(get_base_user_views),
    view_type: UserViewType = Query(default="minimal"),
) -> BaseUserWebCommand:
    if view_type not in views:
        raise WebServiceError(user_message="invalid view type for user")
    return BaseUserWebCommand(view_type=view_type)


BaseUserCommandDep = Annotated[
    BaseUserWebCommand, Depends(get_base_user_command)
]
