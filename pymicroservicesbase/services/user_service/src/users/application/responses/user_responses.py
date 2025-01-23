from typing import TypeVar
from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)

T = TypeVar("T", bound=BaseUserViewModel)


class UserResponseModel(BaseResponseSchema[T]):
    data: T | None = Field(default=None)
