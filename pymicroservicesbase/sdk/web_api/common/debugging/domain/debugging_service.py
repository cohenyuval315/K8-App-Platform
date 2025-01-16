from pymicroservicesbase.sdk.web_api.common.debugging.application.commands.get_debuggers_command import (
    GetDebuggersCommand,
)
from pymicroservicesbase.sdk.web_api.common.debugging.application.commands.start_debugging_command import (
    StartDebuggingCommand,
)


class DebuggingService:
    async def get_debuggers(
        self,
        command: GetDebuggersCommand,
    ):
        return ["debugpy"]

    async def start_debugging(
        self,
        command: StartDebuggingCommand,
    ):
        pass
