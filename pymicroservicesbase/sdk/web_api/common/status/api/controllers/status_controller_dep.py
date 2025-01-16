from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.status.api.controllers.status_controller import (
    StatusController,
)
from pymicroservicesbase.sdk.web_api.common.status.domain.status_service import (
    StatusService,
)


def get_status_controller() -> StatusController:
    return StatusController(StatusService())


StatusControllerDep = Annotated[
    StatusController, Depends(get_status_controller)
]
