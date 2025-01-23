from typing import Annotated, Type

from fastapi import Depends, Query, status
from pydantic import ConfigDict, Field, PrivateAttr

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.user_service.logger import logger
from pymicroservicesbase.services.user_service.src.users.application.schemas.user_views import (
    BaseUserViewModel,
    UserViewType,
    user_views,
)


class BaseUserWebCommand(BaseWebCommand):
    model_config = ConfigDict(
        use_enum_values=True
    )

    _user_view_model: Type[BaseUserViewModel] = PrivateAttr(init=False)

    view_type: UserViewType = Field(
        default=UserViewType.MINIMAL,#"minimal",
        title="view_type",
        description="Defines the view type for the user",
    )

    @classmethod
    def set_view_model(cls, user_view_model: Type[BaseUserViewModel]):
        cls._user_view_model = user_view_model

    @classmethod
    def get_view_model(cls) -> Type[BaseUserViewModel]:
        return cls._user_view_model


async def get_base_user_command(
    view_type: UserViewType = Query(default="minimal"),
) -> BaseUserWebCommand:
    model = user_views.get(view_type, None)
    if model is None:
        logger.error(f"invalid view type for user {view_type}")
        raise WebServiceError(
            error_message=f"invalid view type for user {view_type}",
            error_code=status.HTTP_400_BAD_REQUEST,
        )

    command = BaseUserWebCommand(
        view_type=view_type,
    )
    command.set_view_model(model)
    return command


BaseUserCommandDep = Annotated[
    BaseUserWebCommand, Depends(get_base_user_command)
]
