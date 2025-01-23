from typing import Annotated, Any, List, Type
from fastapi import Query, Depends, status
from pydantic import ConfigDict, Field, ValidationError, ValidatorFunctionWrapHandler, field_validator, model_validator, PrivateAttr

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.user_views import (
    UserViewType,
    user_views,
    BaseUserViewModel
)

from pymicroservicesbase.services.user_service.logger import logger


class BaseUserWebCommand(BaseWebCommand):
    model_config = ConfigDict(
        # arbitrary_types_allowed=True,
    )
    _user_view_model: Type[BaseUserViewModel] = PrivateAttr(init=False)

    view_type: UserViewType = Field(
        default="minimal",
        title="view_type", description="Defines the view type for the user",
    )


    @classmethod
    def set_view_model(cls, user_view_model: Type[BaseUserViewModel]):
        cls._user_view_model = user_view_model

    @classmethod
    def get_view_model(cls) -> Type[BaseUserViewModel]:
        return cls._user_view_model

    # @field_validator('view_type', mode='wrap')
    # @classmethod
    # def ensure_view_type(cls, value: Any, handler: ValidatorFunctionWrapHandler):
    #     try:
    #         model = user_views.get(value, None)
    #         if model is None:
    #             logger.error(f"Invalid user model view type: {value}")
    #             raise WebServiceError(
    #                 error_message=f"Invalid user model view type: {value}",
    #                 error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             )
    #         handler(value)
    #         return model
    #     except ValidationError as err:
    #         raise err




# out of scope , user service does not need to know
# ------------------------------------------------

# async def get_base_user_views(

# ) -> List[UserViewType]:
#     return ["minimal", "admin", "full", "internal", "owner", "public"]


async def get_base_user_command(
    view_type: UserViewType = Query(default="minimal"),
) -> BaseUserWebCommand:
    model = user_views.get(view_type, None)
    if model is None:
        raise WebServiceError(error_message=f"invalid view type for user {view_type}", error_code=400)

    command = BaseUserWebCommand(
        view_type=view_type,
    )
    command.set_view_model(model)
    return command



BaseUserCommandDep = Annotated[
    BaseUserWebCommand, Depends(get_base_user_command)
]
