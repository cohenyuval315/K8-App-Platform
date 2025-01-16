from pydantic import ConfigDict, Field

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class TokensPayload(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    refresh_token: str | None = Field(default=None, alias="refreshToken")
    access_token: str | None = Field(default=None, alias="accessToken")
    session_id: str | None = Field(default=None, alias="sessionId")
    session_token: str | None = Field(default=None, alias="sessionToken")
    id_token: str | None = Field(default=None, alias="idToken")
    csrf_token: str | None = Field(default=None, alias="csrfToken")
