from fastapi import Response
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.services.authentication_service.src.authentication.api.controllers.authentication_controller_dep import (
    AuthenticationControllerDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_user_authentication_data_command import (
    GetUserAuthenticationDataCommandDep,
)

from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.get_product_authentication_data_command import (
    GetProductAuthenticationDataCommandDep,
)


session_router = WebRouter(
    prefix="/sessions",
    tags=["authentication", "sessions"],
)


@session_router.post(
    "/user/{user_id}",
    status_code=200,
)
async def get_user_session_data(
    command: GetUserAuthenticationDataCommandDep,  # TODO replace to session data
    authentication_controller: AuthenticationControllerDep,
) -> Response:
    return await authentication_controller.get_user_authentication_data(
        command
    )


@session_router.post(
    "/product/{product_id}",
    status_code=200,
)
async def get_product_session_data(
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
