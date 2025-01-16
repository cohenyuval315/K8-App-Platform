from fastapi import Path
from typing import Annotated
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class GetHealthCheckCommand(BaseWebCommand):
    health_check: str


async def get_get_health_check_command(health_check: str = Path(...)):
    return GetHealthCheckCommand(health_check=health_check)


GetHealthCheckCommandDep = Annotated[
    GetHealthCheckCommand, get_get_health_check_command
]
