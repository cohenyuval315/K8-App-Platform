from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.run_health_checks_command import (
    RunHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_check_command import (
    GetHealthCheckCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_checks_command import (
    GetHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.domain.health_check_service import (
    HealthCheckService,
)


class HealthCheckController:
    def __init__(self, health_service: HealthCheckService):
        self.health_service = health_service

    async def get_health_check(self, command: GetHealthCheckCommand):
        return await self.health_service.get_health_check(command)

    async def get_health_checks(self, command: GetHealthChecksCommand):
        return await self.health_service.get_health_checks(command)

    async def run_health_checks(self, command: RunHealthChecksCommand):
        return await self.health_service.run_health_checks(command)
