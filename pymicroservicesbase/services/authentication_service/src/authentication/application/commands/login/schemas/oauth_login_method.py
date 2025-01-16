from typing import Literal

from pydantic import Field, EmailStr
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

TwoFactorMethod = Literal["email", "sms"]


class OAuthLoginMethod(BaseModel):
    email: EmailStr = Field(..., description="Minimum password length")
    # oauth_provider: OAuthProvider = Field(..., description="OAuth client ID")
    # client_id: str = Field(..., description="OAuth client ID")
    # client_secret: str = Field(..., description="OAuth client secret")
    # redirect_uri: AnyUrl = Field(..., description="OAuth redirect URI")
