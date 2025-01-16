from typing import Any

from pymicroservicesbase.services.user_service.src.users.domain.services.user_service import (
    UserService,
)
from pymicroservicesbase.services.user_service.src.users.application import (
    DeleteUserCommand,
    GetManyUsersCommand,
    GetUserCommand,
    UpdateUserCommand,
    CreateUserCommand,
    UserResponseModel,
    UsersResponseModel,
)

from pymicroservicesbase.services.user_service.logger import logger  # noqa


class UserController:
    def __init__(self, user_service: UserService) -> None:
        self.user_service: UserService = user_service

    async def create_user(
        self, command: CreateUserCommand
    ) -> UserResponseModel:
        return await self.user_service.create_user(command)

    async def update_user(
        self, command: UpdateUserCommand
    ) -> UserResponseModel:
        return await self.user_service.update_user(command)

    async def delete_user(self, command: DeleteUserCommand) -> Any:
        return await self.user_service.delete_user(command)

    async def get_user(self, command: GetUserCommand) -> UserResponseModel:
        return await self.user_service.get_user(command)

    async def get_many_users(
        self, command: GetManyUsersCommand
    ) -> UsersResponseModel:
        return await self.user_service.get_many_users(command)
