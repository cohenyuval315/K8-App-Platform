from typing import Any
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.common.debugging.api.controllers.debugging_controller_dep import (
    DebuggingControllerDep,
)
from pymicroservicesbase.sdk.web_api.common.debugging.application.commands.get_debuggers_command import (
    GetDebuggersCommand,
)


debugging_router = WebRouter(prefix="/debugging", tags=["debugging"])


@debugging_router.get(
    "",
    status_code=200,
)
async def get_debuggers(
    command: GetDebuggersCommand, controller: DebuggingControllerDep
) -> Any:
    return await controller.get_debuggers(command)
