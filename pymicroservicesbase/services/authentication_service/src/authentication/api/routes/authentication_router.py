from typing import Any
from fastapi import Response
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.services.authentication_service.src.authentication.api.controllers.authentication_controller_dep import (
    AuthenticationControllerDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.api.routes.session_router import (
    session_router,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.login.login_command import (
    LoginCommandDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.verify_command import (
    VerifyCommandDep,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.whoami_command import (
    WhoAmICommandDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.refresh.refresh_command import (
    RefreshCommandDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_user_authentication_data_command import (
    GetUserAuthenticationDataCommandDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_product_authentication_data_command import (
    GetProductAuthenticationDataCommandDep,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.refresh_responses import (
    RefreshResponseModel,
)


from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.logout.logout_command import (
    LogoutCommandDep,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.register.register_command import (
    RegisterCommandDep,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.login_responses import (
    LoginResponseModel,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.logout_responses import (
    LogoutResponseModel,
)


from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.register_responses import (
    RegisterResponseModel,
)


authentication_router = WebRouter(
    prefix="/auth",
    tags=["authentication"],
)
authentication_router.include_router(session_router)


@authentication_router.post(
    "/register", status_code=200, response_model=RegisterResponseModel
)
async def register(
    command: RegisterCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> RegisterResponseModel:
    return await authentication_controller.register(command)


@authentication_router.post(
    "/confirm",
    status_code=200,
    # response_model=RegisterResponseModel
)
async def confirm(
    command: RegisterCommandDep,
    authentication_controller: AuthenticationControllerDep,
):
    return await authentication_controller.confirm_registration()


@authentication_router.post(
    "/login", status_code=200, response_model=LoginResponseModel
)
async def login(
    command: LoginCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> LoginResponseModel | Response:
    return await authentication_controller.login(command)


@authentication_router.post(
    "/logout", status_code=200, response_model=LogoutResponseModel
)
async def logout(
    command: LogoutCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> LogoutResponseModel | Response:
    return await authentication_controller.logout(command)


@authentication_router.post(
    "/refresh", status_code=200, response_model=RefreshResponseModel
)
async def refresh(
    command: RefreshCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> RefreshResponseModel | Response:
    return await authentication_controller.refresh(command)


@authentication_router.post(
    "/verify",
    status_code=200,
)
async def verify(
    command: VerifyCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> Response:
    return await authentication_controller.verify(command)


@authentication_router.post(
    "/session/{user_id}",
    status_code=200,
)
async def get_user_authentication_data(
    command: GetUserAuthenticationDataCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> Response:
    return await authentication_controller.get_user_authentication_data(
        command
    )


@authentication_router.post(
    "/product/{product_id}",
    status_code=200,
)
async def get_product_authentication_data(
    command: GetProductAuthenticationDataCommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> Response:
    return await authentication_controller.get_product_authentication_data(
        command
    )


# @authentication_router.post(
#     "/authenticate",
#     status_code=200,
#     response_model=AuthenticationResponseModel
# )
# async def authenticate(
#     command: AuthenticationCommand,
#     authentication_controller: AuthenticationControllerDep,
# ) -> AuthenticationResponseModel | None:
#     return await authentication_controller.authenticate(command)


@authentication_router.get("/whoami", status_code=200, response_model=Any)
async def whoami(
    command: WhoAmICommandDep,
    authentication_controller: AuthenticationControllerDep,
) -> Any:
    return await authentication_controller.whoami(command)


# @authentication_router.post(
#     "/recovery",
#     status_code=200,
#     response_model=AccountRecoveryResponseModel
# )
# async def account_recovery(
#     command:AccountRecoveryCommand,
#     authentication_controller: AuthenticationControllerDep,
# ) -> AccountRecoveryResponseModel:
#     return await authentication_controller.account_recovery(command)
