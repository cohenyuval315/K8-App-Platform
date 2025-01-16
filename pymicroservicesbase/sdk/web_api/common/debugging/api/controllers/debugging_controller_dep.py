from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.debugging.api.controllers.debugging_controller import (
    DebuggingController,
)
from pymicroservicesbase.sdk.web_api.common.debugging.domain.debugging_service import (
    DebuggingService,
)


def get_debugging_controller() -> DebuggingController:
    return DebuggingController(DebuggingService())


DebuggingControllerDep = Annotated[
    DebuggingController, Depends(get_debugging_controller)
]
