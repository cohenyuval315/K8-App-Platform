from typing import TypedDict


class HealthCheck(TypedDict):
    name: str
    timeout: int
