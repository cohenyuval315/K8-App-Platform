from typing import Annotated, List, TypedDict

from fastapi import Body
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class RunHealthCheckRetryPolicy(TypedDict):
    retries: int
    backoff: int


class RunHealthCheck(TypedDict):
    name: str
    retry_policy: RunHealthCheckRetryPolicy


class RunHealthChecksCommand(BaseWebCommand):
    health_checks: List[RunHealthCheck]


async def get_run_health_checks_command(
    health_checks: List[RunHealthCheck] = Body(embed=True),
):
    return RunHealthChecksCommand(health_checks=health_checks)


RunHealthChecksCommandDep = Annotated[
    RunHealthChecksCommand, get_run_health_checks_command
]
