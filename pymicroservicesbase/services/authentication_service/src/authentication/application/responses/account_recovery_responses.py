from typing import Any, List

from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class AccountRecoveryResponseModel(BaseResponseSchema[Any]):
    data: List[Any] | None = Field(default=None)
