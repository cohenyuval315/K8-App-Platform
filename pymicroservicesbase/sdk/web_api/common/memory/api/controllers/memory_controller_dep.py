from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.memory.api.controllers.memory_controller import (
    MemoryController,
)
from pymicroservicesbase.sdk.web_api.common.memory.domain.memory_service import (
    MemoryService,
)


def get_memory_controller() -> MemoryController:
    return MemoryController(MemoryService())


MemoryControllerDep = Annotated[
    MemoryController, Depends(get_memory_controller)
]
