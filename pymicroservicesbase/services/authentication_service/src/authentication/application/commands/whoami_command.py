from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from typing import Annotated
from fastapi import Depends, Request, Response
from pydantic import ConfigDict


class WhoAmICommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
    request: Request
    response: Response


async def get_whoami_command(
    request: Request,
    response: Response,
) -> WhoAmICommand:
    return WhoAmICommand(request=request, response=response)


WhoAmICommandDep = Annotated[WhoAmICommand, Depends(get_whoami_command)]
