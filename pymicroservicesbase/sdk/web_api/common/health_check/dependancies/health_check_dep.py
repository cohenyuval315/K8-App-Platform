from typing import Annotated, Dict, Callable
from fastapi import Depends
from .health_check_status import HealthCheckStatus


def get_health_check(health_check: str):
    pass


def get_health_checks(health_check: str):
    pass


HealthChecksDep = Annotated[
    Dict[str, Callable[..., HealthCheckStatus]], Depends(get_health_checks)
]

HealthChecksDep = Annotated[
    Callable[..., HealthCheckStatus], Depends(get_health_check)
]

HealthChecksHealthyDep = Annotated[bool, Depends(get_health_checks)]
