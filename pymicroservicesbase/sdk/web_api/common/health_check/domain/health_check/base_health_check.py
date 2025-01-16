from abc import ABC, abstractmethod
from .health_check_status import HealthCheckStatus

# from ..exceptions import HealthCheckAlreadyRunningError
import time


class BaseHealthCheck(ABC):
    def __init__(self, name: str, timeout: int):
        self.name = name
        self.timeout = timeout
        self._is_running = False
        self.start_time = time.time()

    @abstractmethod
    async def health_check(self) -> HealthCheckStatus:
        """health check"""

    def get_is_running(self):
        return self._is_running

    async def run_test(self) -> HealthCheckStatus:
        if self._is_running is True:
            return HealthCheckStatus(name=self.name, status="InProgress")
        try:
            self._is_running = True
            result = await self.health_check()
            elapsed_time = self.start_time - time.time()

        except Exception as e:
            return HealthCheckStatus(
                name=self.name, status="Not Healthy", details=e
            )
        else:
            return HealthCheckStatus(
                name=self.name,
                status="Healthy",
                details={"elapsed_time": elapsed_time, "result": result},
            )
        finally:
            self._is_running = False
