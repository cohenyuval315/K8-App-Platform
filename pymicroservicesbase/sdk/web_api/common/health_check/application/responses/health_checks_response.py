from typing import List
from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class HealthChecksResponse(BaseResponseSchema[List[str]]):
    data: List[str] | None = None
