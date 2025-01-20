from typing import List
from pymicroservicesbase.sdk.web_api.common.health_check.health_checks.health_check_ping import (
    HealthCheckStatus,
)
from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class HealthChecksStatusResponse(BaseResponseSchema[List[HealthCheckStatus]]):
    data: List[HealthCheckStatus] | None = None
