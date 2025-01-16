from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.health_check.api.controllers.health_check_controller import (
    HealthCheckController,
)
from pymicroservicesbase.sdk.web_api.common.health_check.domain.health_check_service import (
    HealthCheckService,
)


def get_health_check_controller() -> HealthCheckController:
    return HealthCheckController(HealthCheckService([], []))


HealthCheckControllerDep = Annotated[
    HealthCheckController, Depends(get_health_check_controller)
]
