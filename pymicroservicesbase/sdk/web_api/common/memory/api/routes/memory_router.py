from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.common.memory.api.controllers.memory_controller_dep import (
    MemoryControllerDep,
)
from pymicroservicesbase.sdk.web_api.common.memory.application.responses.memory_response import (
    MemoryResponse,
)
from pymicroservicesbase.sdk.web_api.common.memory.application.commands.get_memory_command import (
    GetMemoryCommand,
)


memory_router = WebRouter(prefix="/memory", tags=["memory"])


@memory_router.get("", status_code=200, response_model=MemoryResponse)
async def get_memory(
    command: GetMemoryCommand, memory_controller: MemoryControllerDep
) -> MemoryResponse:
    return await memory_controller.get_memory(command)
