from typing import Any
from pymicroservicesbase.services.user_service.src.users.application import (
    UserResponseModel,
    UsersResponseModel,
)

from pymicroservicesbase.services.user_service.src.users.api.controllers.user_controller_dep import (
    UserControllerDep,
)
from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.create_user_command import (
    CreateUserCommandDep,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.delete_user.delete_user_command import (
    DeleteUserCommandDep,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.get_many_users.get_many_users_command import (
    GetManyUsersCommandDep,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.get_user.get_user_command import (
    GetUserCommandDep,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.update_user.update_user_command import (
    UpdateUserCommandDep,
)


product_router = WebRouter(
    prefix="/users",
    tags=["users"],
)


@product_router.post(
    path="",
    response_model=UserResponseModel,
    status_code=201,
    response_model_exclude_none=False,
    response_model_exclude_unset=False,
    response_model_exclude_defaults=True,
)
async def create_user(
    user_controller: UserControllerDep,
    command: CreateUserCommandDep,
) -> UserResponseModel:
    """
    Create a new user.
    """
    return await user_controller.create_user(command)


@product_router.get(
    "/{user_id}",
    response_model=UserResponseModel,
    status_code=200,
)
async def get_user(
    user_controller: UserControllerDep, command: GetUserCommandDep
) -> UserResponseModel:
    """
    Retrieve a user by their ID.
    """
    return await user_controller.get_user(command)


@product_router.put(
    "/{user_id}",
    response_model=UserResponseModel,
    status_code=200,
)
async def update_user(
    user_controller: UserControllerDep, command: UpdateUserCommandDep
) -> UserResponseModel:
    """
    Update a user's information.
    """

    return await user_controller.update_user(command)


@product_router.delete(
    "/{user_id}",
    status_code=200,
)
async def delete_user(
    user_controller: UserControllerDep, command: DeleteUserCommandDep
) -> Any:
    """
    Delete a user by their ID.
    """
    return await user_controller.delete_user(command)


@product_router.get(
    "/",
    response_model=UsersResponseModel,
    status_code=200,
)
async def get_many_users(
    user_controller: UserControllerDep, command: GetManyUsersCommandDep
) -> UsersResponseModel:
    """
    Retrieve a list of users with pagination.
    """
    return await user_controller.get_many_users(command)
