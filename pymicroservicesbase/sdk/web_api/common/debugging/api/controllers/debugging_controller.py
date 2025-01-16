from typing import Any
from pymicroservicesbase.sdk.web_api.common.debugging.domain.debugging_service import (
    DebuggingService,
)
from pymicroservicesbase.sdk.web_api.common.debugging.application.commands.get_debuggers_command import (
    GetDebuggersCommand,
)
from pymicroservicesbase.sdk.web_api.common.debugging.application.commands.start_debugging_command import (
    StartDebuggingCommand,
)


class DebuggingController:
    def __init__(self, debugging_service: DebuggingService):
        self.debugging_service = debugging_service

    async def get_debuggers(
        self,
        command: GetDebuggersCommand,
    ) -> Any:
        return await self.debugging_service.get_debuggers(command)

    async def start_debugging(
        self,
        command: StartDebuggingCommand,
    ) -> Any:
        # return await self.debugging_service.get_debuggers(command)
        pass
