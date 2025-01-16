from typing import Annotated

from fastapi import Body
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class RaiseErrorCommand(BaseWebCommand):
    error_type: str


async def get_raise_error_command(error_type: str = Body(default="exception")):
    return RaiseErrorCommand(error_type=error_type)


RaiseErrorCommandDep = Annotated[RaiseErrorCommand, get_raise_error_command]
