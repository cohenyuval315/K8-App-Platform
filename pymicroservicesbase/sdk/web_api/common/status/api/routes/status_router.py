from typing import Any
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.common.status.api.controllers.status_controller_dep import (
    StatusControllerDep,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_uptime_command import (
    GetUptimeCommand,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.get_version_command import (
    GetVersionCommand,
)
from pymicroservicesbase.sdk.web_api.common.status.application.commands.raise_error_command import (
    RaiseErrorCommandDep,
)


status_router = WebRouter(
    prefix="/status",
    tags=["status"],
)


@status_router.get(
    "/ping",
    summary="ping",
    response_description="ping",
    status_code=200,
    response_model=Any,
)
async def ping(status_controller: StatusControllerDep):
    return await status_controller.ping()


@status_router.get(
    "/uptime",
    summary="Uptime",
    response_description="Server uptime",
    status_code=200,
    response_model=Any,
)
async def get_uptime(
    command: GetUptimeCommand,
    status_controller: StatusControllerDep,
):
    return await status_controller.get_uptime(command)


@status_router.get(
    "/version",
    summary="Version info",
    response_description="Version details",
    status_code=200,
    response_model=Any,
)
async def version(
    command: GetVersionCommand, status_controller: StatusControllerDep
):
    return await status_controller.get_version(command)


@status_router.post(
    "/error",
    summary="Error",
    response_description="error details",
    status_code=200,
    response_model=Any,
)
async def error(
    command: RaiseErrorCommandDep, status_controller: StatusControllerDep
):
    return await status_controller.raise_error(command)
