from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.run_health_checks_command import (
    RunHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_check_command import (
    GetHealthCheckCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_checks_command import (
    GetHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_check_response import (
    HealthCheckResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_response import (
    HealthChecksResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_status_response import (
    HealthChecksStatusResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.domain.health_check_service import (
    HealthCheckService,
)


class HealthCheckController:
    def __init__(self, health_service: HealthCheckService):
        self.health_service = health_service

    async def get_health_check(
        self, health_check: str, command: GetHealthCheckCommand
    ) -> HealthCheckResponse:
        return await self.health_service.get_health_check(
            health_check, command
        )

    async def get_health_checks(
        self, command: GetHealthChecksCommand
    ) -> HealthChecksResponse:
        return await self.health_service.get_health_checks(command)

    async def run_health_checks(
        self, health_checks, command: RunHealthChecksCommand
    ) -> HealthChecksStatusResponse:
        return await self.health_service.run_health_checks(command)
