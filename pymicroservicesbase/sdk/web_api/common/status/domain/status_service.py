from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_uptime_command import (
    GetUptimeCommand,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_version_command import (
    GetVersionCommand,
)

from pymicroservicesbase.sdk.web_api.common.status.application.commands.raise_error_command import (
    RaiseErrorCommand,
)


class StatusService:
    def __init__(self):
        self.error_map = {
            "exception": Exception,
        }

    async def ping(self):
        return {"message": "pong!"}

    async def get_uptime(self, command: GetUptimeCommand):
        return {"uptime_seconds": 0}

    async def get_version(self, command: GetVersionCommand):
        return {"version": 0}

    async def raise_error(self, command: RaiseErrorCommand):
        # Get the exception class from the error_map
        error_class = self.error_map.get(command.error_type)
        if error_class:
            raise error_class(
                f"An error of type '{command.error_type}' occurred."
            )
        else:
            # Handle unknown error types
            raise Exception(f"Unknown error type: {command.error_type}")
