from fastapi import Response
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_product_authentication_data_command import (
    GetProductAuthenticationDataCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_user_authentication_data_command import (
    GetUserAuthenticationDataCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.logout.logout_command import (
    LogoutCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.register.register_command import (
    RegisterCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.verify_command import (
    VerifyCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.whoami_command import (
    WhoAmICommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.authentication_service import (
    AuthenticationService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.logout_responses import (
    LogoutResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.login_responses import (
    LoginResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.register_responses import (
    RegisterResponseModel,
)
from pymicroservicesbase.services.authentication_service.logger import logger

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.refresh.refresh_command import (
    RefreshCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.refresh_responses import (
    RefreshResponseModel,
)


class AuthenticationController:
    def __init__(self, authentication_service: AuthenticationService):
        self.authentication_service = authentication_service

    async def register(
        self, command: RegisterCommand
    ) -> RegisterResponseModel:
        return await self.authentication_service.register(command)

    async def refresh(
        self,
        command: RefreshCommand,
    ) -> RefreshResponseModel | Response:
        return await self.authentication_service.refresh(command)

    async def login(
        self, command: LoginCommand
    ) -> LoginResponseModel | Response:
        return await self.authentication_service.login(command)

    async def logout(
        self, command: LogoutCommand
    ) -> LogoutResponseModel | Response:
        return await self.authentication_service.logout(command)

    async def verify(self, command: VerifyCommand) -> Response:
        res = await self.authentication_service.verify(command)
        logger.debug(res.headers)
        return res

    async def confirm_registration(self):
        token = ""
        return await self.authentication_service.confirm_registration(token)

    # async def authenticate(self, command: AuthenticationCommand) -> AuthenticationResponseModel:
    #     return await self.authentication_service.authenticate(command)

    async def whoami(self, command: WhoAmICommand):
        return await self.authentication_service.whoami(command)

    # async def account_recovery(self, command:AccountRecoveryCommand) -> AccountRecoveryResponseModel:
    #     return await self.authentication_service.account_recovery(command)

    async def get_user_authentication_data(
        self, command: GetUserAuthenticationDataCommand
    ):
        return await self.authentication_service.get_user_authentication_data(
            command
        )

    async def get_product_authentication_data(
        self, command: GetProductAuthenticationDataCommand
    ):
        return (
            await self.authentication_service.get_product_authentication_data(
                command
            )
        )
