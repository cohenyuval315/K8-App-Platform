from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)

from typing import List


class ConfigurationsResponse(BaseResponseSchema[List[str]]):
    data: List[str] | None = None
