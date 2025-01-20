from typing import Literal, Any

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class HealthCheckStatus(BaseModel):
    name: str
    status: Literal["Healthy", "Not Healthy", "InProgress"]
    details: Any | None = None
    error: Any | None = None
