from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class RefreshTokenLoginMethod(BaseModel):
    refresh_token: str = Field(..., description="")
