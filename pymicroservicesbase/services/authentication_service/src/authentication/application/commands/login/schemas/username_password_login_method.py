from typing import Callable, Set, Literal

from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

TwoFactorMethod = Literal["email", "sms"]


class UsernamePasswordLoginMethod(BaseModel):
    username: int = Field(..., description="Minimum password length")
    password: int = Field(..., description="Maximum password length")
    two_factor_enabled: bool | Callable[..., bool] = Field(
        ...,
        description="Indicates if 2FA is enabled, disabled, or conditional",
    )
    two_factor_options: Set[TwoFactorMethod] = Field(
        ..., description="List of 2FA methods (e.g., 'email', 'phone')"
    )
    two_factor_timeout: int = Field(
        ..., description="Timeout for 2FA verification in seconds"
    )
