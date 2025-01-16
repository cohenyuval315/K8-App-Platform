from typing import Any

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)
from pydantic import Field


class RegisterResponseModel(BaseResponseSchema[Any]):
    data: Any | None = Field(default=None)
