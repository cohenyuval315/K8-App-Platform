from typing import Annotated
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class GetHealthChecksCommand(BaseWebCommand):
    pass


async def get_get_health_checks_command():
    return GetHealthChecksCommand()


GetHealthChecksCommandDep = Annotated[
    GetHealthChecksCommand, get_get_health_checks_command
]
