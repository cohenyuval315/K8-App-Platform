from typing import List, TypeVar

from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)

from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
)

T = TypeVar("T", bound=BaseUserModel)


class UsersResponseModel(BaseResponseSchema[List[T]]):
    data: List[T] | None = Field(default=None)
