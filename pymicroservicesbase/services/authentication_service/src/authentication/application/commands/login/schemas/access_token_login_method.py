from pydantic import Field
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)


class AccessTokenLoginMethod(LoginCommand):
    access_token: str = Field(..., description="")
