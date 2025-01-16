from typing import Any, List

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class MemoryResponse(BaseResponseSchema[List[Any]]):
    data: List[Any] | None = None
