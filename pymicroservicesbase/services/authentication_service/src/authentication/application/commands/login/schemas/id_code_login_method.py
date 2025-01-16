from pydantic import Field
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)


class IDCodeLoginMethod(LoginCommand):
    ID: int = Field(..., description="Minimum password length")
    code: int = Field(..., description="Maximum password length")
    # confirmation: ConfirmationConfig = Field()
    # two_factor_options: Set[TwoFactorMethod] = Field(..., description="List of 2FA methods (e.g., 'email', 'phone')")
    # two_factor_timeout: int = Field(..., description="Timeout for 2FA verification in seconds")
