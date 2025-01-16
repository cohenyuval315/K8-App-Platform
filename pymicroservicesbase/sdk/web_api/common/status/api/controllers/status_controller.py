from pymicroservicesbase.sdk.web_api.common.status.application.commands.raise_error_command import (
    RaiseErrorCommand,
)
from pymicroservicesbase.sdk.web_api.common.status.domain.status_service import (
    StatusService,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_uptime_command import (
    GetUptimeCommand,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_version_command import (
    GetVersionCommand,
)


class StatusController:
    def __init__(self, status_service: StatusService):
        self.status_service = status_service

    async def ping(self):
        return await self.status_service.ping()

    async def get_uptime(self, command: GetUptimeCommand):
        return await self.status_service.get_uptime(command)

    async def get_version(self, command: GetVersionCommand):
        return await self.status_service.get_version(command)

    async def raise_error(self, command: RaiseErrorCommand):
        return await self.status_service.raise_error(command)
