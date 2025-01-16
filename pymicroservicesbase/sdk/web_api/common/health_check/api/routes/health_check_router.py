from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter

from pymicroservicesbase.sdk.web_api.common.health_check.api.controllers.health_check_controller_dep import (
    HealthCheckControllerDep,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.run_health_checks_command import (
    RunHealthChecksCommandDep,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_check_command import (
    GetHealthCheckCommandDep,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_checks_command import (
    GetHealthChecksCommandDep,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_check_response import (
    HealthCheckResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_response import (
    HealthChecksResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_status_response import (
    HealthChecksStatusResponse,
)

health_check_router = WebRouter(prefix="/health", tags=["health_check"])


@health_check_router.get(
    "",
    status_code=200,
    response_model=HealthChecksResponse,
)
async def get_health_checks(
    command: GetHealthChecksCommandDep,
    health_check_controller: HealthCheckControllerDep,
) -> HealthChecksResponse:
    return await health_check_controller.get_health_checks(command)


@health_check_router.get(
    "/{health_check}", response_model=HealthCheckResponse, status_code=200
)
async def get_health_check(
    health_check: str,
    command: GetHealthCheckCommandDep,
    health_check_controller: HealthCheckControllerDep,
) -> HealthCheckResponse:
    return await health_check_controller.get_health_check(
        health_check, command
    )


@health_check_router.post(
    "",
    status_code=200,
    response_model=HealthChecksStatusResponse,
)
async def run_health_checks(
    health_checks: str,
    command: RunHealthChecksCommandDep,
    health_check_controller: HealthCheckControllerDep,
) -> HealthChecksStatusResponse:
    return await health_check_controller.run_health_checks(
        health_checks, command
    )
