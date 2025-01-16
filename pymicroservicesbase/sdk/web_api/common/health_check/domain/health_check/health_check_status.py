from typing import Literal, Any

from ...core_api.base_model import BaseModel
from fastapi import Path


class HealthCheckStatus(BaseModel):
    name: str
    status: Literal["Healthy", "Not Healthy", "InProgress"]
    details: Any | None = None
    error: Any | None = None
    Path()
