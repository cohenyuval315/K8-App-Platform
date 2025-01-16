from pydantic import ConfigDict, Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class UserPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")
    user_id: str = Field(..., alias="id")
    user_email: str = Field(..., alias="email")
    user_username: str = Field(..., alias="username")
