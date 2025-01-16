from pymicroservicesbase.sdk.web_api.common.memory.application.responses.memory_response import (
    MemoryResponse,
)
from pymicroservicesbase.sdk.web_api.common.memory.application.commands.get_memory_command import (
    GetMemoryCommand,
)


class MemoryService:
    async def get_memory(self, command: GetMemoryCommand) -> MemoryResponse:
        pass
