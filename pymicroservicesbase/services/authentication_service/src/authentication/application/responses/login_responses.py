from typing import Any

from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class LoginResponseModel(BaseResponseSchema[Any]):
    data: Any | None = Field(default=None)
