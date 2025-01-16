from typing import List
from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


from pymicroservicesbase.sdk.web_api.common.health_check.health_check_status import (
    HealthCheckStatus,
)


class HealthChecksStatusResponse(BaseResponseSchema[List[HealthCheckStatus]]):
    data: List[HealthCheckStatus] | None = None
