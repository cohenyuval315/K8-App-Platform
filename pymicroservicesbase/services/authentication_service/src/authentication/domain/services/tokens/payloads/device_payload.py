from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class DevicePayload(BaseModel):
    device_id: str = Field(..., description="")
    user_agent: str = Field(..., description="")
    ip_address: str = Field(..., description="")
