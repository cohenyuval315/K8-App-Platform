from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class AccessPayload(BaseModel):
    client_id: str = Field(...)
    client_secret: str = Field(...)
    scope: str = Field(...)
