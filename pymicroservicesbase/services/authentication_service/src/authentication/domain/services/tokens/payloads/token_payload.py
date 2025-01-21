from pydantic import Field

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class TokenPayload(BaseModel):
    token_title: str = Field(...)
    token_value: str = Field(...)
    token_expire: str = Field(...)
    token_type: str = Field(...)
