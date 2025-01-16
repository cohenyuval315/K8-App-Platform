from pydantic import ConfigDict, Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


# devices: List[DevicePayload] = Field(..., description="many devices that uses this session id - should not be more then 1 unless proxy or user agent, so list")
class UserSessionData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=False, extra="allow")
    # user_agent:str = Field(..., description="")
    # ip:str = Field(..., description="")
    # devices
    last_activity: str = Field(..., description="")
    user_id: str = Field(..., description="")
    user_email: str = Field(..., description="")
    user_username: str = Field(..., description="")
    product_id: str = Field(..., description="")
    extend_count: int = Field(..., description="")
    session_id: str = Field(..., description="")
    # csrf_token: str = Field(..., description="")
    # expire_at: datetime = Field(..., description="")
    # ttl: int = Field(..., description="")
