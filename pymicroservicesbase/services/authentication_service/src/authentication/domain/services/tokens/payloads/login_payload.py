from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class LoginPayload(BaseModel):
    login_method: str = Field(...)
    login_provider: str | None = Field(default=None)
