from ..health_check_status import HealthCheckStatus
from ..base_health_check import BaseHealthCheck


class HealthCheckPing(BaseHealthCheck):
    def __init__(self, timeout: int):
        super().__init__("ping", timeout)

    async def health_check(self) -> HealthCheckStatus:
        """health check"""
        return HealthCheckStatus(name=self.name, status="Healthy")
