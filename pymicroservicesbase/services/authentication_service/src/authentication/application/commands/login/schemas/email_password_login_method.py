from pydantic import Field, EmailStr

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)


class EmailPasswordLoginMethod(LoginCommand):
    email: EmailStr = Field(..., description="Minimum password length")
    password: str = Field(..., description="Maximum password length")
