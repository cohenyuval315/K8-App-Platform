from pymicroservicesbase.sdk.web_api.common.memory.domain.memory_service import (
    MemoryService,
)
from pymicroservicesbase.sdk.web_api.common.memory.application.responses.memory_response import (
    MemoryResponse,
)
from pymicroservicesbase.sdk.web_api.common.memory.application.commands.get_memory_command import (
    GetMemoryCommand,
)


class MemoryController:
    def __init__(self, memory_service: MemoryService):
        super().__init__()
        self.memory_service = memory_service

    async def get_memory(
        self,
        command: GetMemoryCommand,
    ) -> MemoryResponse:
        return await self.memory_service.get_memory(command)
