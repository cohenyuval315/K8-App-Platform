from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_user_identity_command import (
    GetUserIdentityCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.logout.logout_command import (
    LogoutCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.refresh.refresh_command import (
    RefreshCommand,
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

<<<<<<< Updated upstream
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.identity_service.identity_service import IdentityService
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.login_service.login_service import LoginService
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.logout_service.logout_service import LogoutService
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.refresh_service.refresh_service import RefreshService
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.signup_service.signup_service import SignupService
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.verify_service.verify_service import VerifyService
=======
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.identity_service.identity_service import (
    IdentityService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.login_service.login_service import (
    LoginService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.logout_service.logout_service import (
    LogoutService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.refresh_service.refresh_service import (
    RefreshService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.signup_service.signup_service import (
    SignupService,
)
from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.verify_service.verify_service import (
    VerifyService,
)
>>>>>>> Stashed changes


class AuthenticationService:
    def __init__(
        self,
<<<<<<< Updated upstream
        login_service:LoginService,
        signup_service:SignupService,
        refresh_service:RefreshService,
=======
        login_service: LoginService,
        signup_service: SignupService,
        refresh_service: RefreshService,
>>>>>>> Stashed changes
        verify_service: VerifyService,
        logout_service: LogoutService,
        identity_service: IdentityService,
    ):
        self.login_service = login_service
        self.signup_service = signup_service
        self.verify_service = verify_service
        self.refresh_service = refresh_service
        self.logout_service = logout_service
        self.identity_service = identity_service

<<<<<<< Updated upstream

    async def register(self, command: RegisterCommand):
        return await self.signup_service.signup(command)

    async def login(self, command: LoginCommand):
        return await self.login_service.login(command)

=======
    async def register(self, command: RegisterCommand):
        return await self.signup_service.signup(command)

    async def login(self, command: LoginCommand):
        return await self.login_service.login(command)

>>>>>>> Stashed changes
    async def logout(self, command: LogoutCommand):
        return await self.logout_service.logout(command)

    async def verify(self, command: VerifyCommand):
        return await self.verify_service.verify(command)

    async def refresh(self, command: RefreshCommand):
        return await self.refresh_service.refresh(command)
<<<<<<< Updated upstream

    async def whoami(self, command: WhoAmICommand):
        return await self.identity_service.whoami(command)

    async def get_user_authentication_data(self, command: GetUserIdentityCommand):
=======

    async def whoami(self, command: WhoAmICommand):
        return await self.identity_service.whoami(command)

    async def get_user_authentication_data(
        self, command: GetUserIdentityCommand
    ):
>>>>>>> Stashed changes
        return await self.identity_service.get_user_identity(command)
