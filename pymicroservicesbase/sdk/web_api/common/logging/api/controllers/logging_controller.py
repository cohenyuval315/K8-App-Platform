from pymicroservicesbase.sdk.web_api.common.logging.domain.logging_service import (
    LoggingService,
)
from pymicroservicesbase.sdk.web_api.common.logging.application.commands.get_logs_command import (
    GetLogsCommand,
)


class LoggingController:
    def __init__(self, logging_service: LoggingService):
        self.logging_service = logging_service

    async def get_logs(self, command: GetLogsCommand):
        return await self.logging_service.get_logs(command)
