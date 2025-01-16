from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.logging.api.controllers.logging_controller import (
    LoggingController,
)
from pymicroservicesbase.sdk.web_api.common.logging.domain.logging_service import (
    LoggingService,
)


def get_logging_controller() -> LoggingController:
    return LoggingController(LoggingService())


LoggingControllerDep = Annotated[
    LoggingController, Depends(get_logging_controller)
]
