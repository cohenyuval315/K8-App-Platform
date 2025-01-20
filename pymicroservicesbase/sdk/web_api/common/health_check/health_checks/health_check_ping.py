# from ..health_check_status import HealthCheckStatus
# from .base_health_check import BaseHealthCheck


from pymicroservicesbase.sdk.web_api.common.health_check import BaseHealthCheck
from pymicroservicesbase.sdk.web_api.common.health_check.domain.health_check.base_health_check import (
    HealthCheckStatus,
)


class HealthCheckPing(BaseHealthCheck):
    def __init__(self, timeout: int):
        super().__init__("ping", timeout)

    async def health_check(self) -> HealthCheckStatus:
        """health check"""
        return HealthCheckStatus(name=self.name, status="Healthy")
