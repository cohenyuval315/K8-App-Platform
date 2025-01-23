from typing import Any, List, Sequence
import bcrypt
from fastapi import status
from pydantic import TypeAdapter
from pydantic_core import PydanticSerializationError

from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.user_service.logger import logger  # noqa
from pymicroservicesbase.services.user_service.src.database.repositories.user_repository import (
    UserRepository,
)
from pymicroservicesbase.services.user_service.src.users.application import (
    CreateUserCommand,
    DeleteUserCommand,
    GetManyUsersCommand,
    GetUserCommand,
    UpdateUserCommand,
    UserResponseModel,
    UsersResponseModel,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.base_user_web_command import (
    BaseUserWebCommand,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.user_views import (
    user_views,
)

from pymicroservicesbase.utils.security.password import hash_password


# from services.user_microservice.user_microservice.users.utils.security import
# from pymicroservicesbase.services.user_service.logger import logger
from sqlalchemy.exc import NoResultFound
from pymicroservicesbase.services.user_service.src.database.connection import (
    db,
)


class UserService:
    def __init__(self, repository: UserRepository):
        self.user_repository = repository
        logger.debug("UserService initialized with UserRepository")


    @db.transactional()
    async def create_user(
        self, command: CreateUserCommand
    ) -> UserResponseModel:
        logger.info("Starting user creation process.")
        try:
            new_user_data = command.data.model_dump(exclude_unset=True)
            logger.debug(f"Received user data for creation: {new_user_data}")
        except PydanticSerializationError:
            logger.error("Data parsing error during user creation.")
            raise WebServiceError(
                title="Parsing Error",
                user_message="Data is required to create a user.",
                error_code=status.HTTP_400_BAD_REQUEST,
            )
        try:
            password = new_user_data.pop("password")
            logger.debug("Extracted password from user data.")
        except KeyError:
            logger.error("Password is missing while creating user.")
            raise WebServiceError(
                title="Password Missing",
                user_message="Password is required to create a user.",
                error_code=status.HTTP_400_BAD_REQUEST,
            )
        else:
            salt = bcrypt.gensalt()
            new_user_data["hashed_password"] = hash_password(password, salt)
            new_user_data["password_salt"] = salt
            logger.debug("Password hashed and added to user data.")
            new_user = await self.user_repository.create(new_user_data)
            logger.info(f"User created successfully with ID: {new_user.id}")
            user_data = self._to_user_representation(new_user, command)
            return UserResponseModel(
                data=user_data, message="User successfully created!"
            )

    async def get_user(self, command: GetUserCommand) -> UserResponseModel:
        logger.info(f"Fetching user with ID: {command.user_id}")
        try:
            user = await self.user_repository.get_user_by_id(command.user_id)
            logger.debug(f"User data retrieved: {user}")
        except NoResultFound:
            logger.error(f"User with ID {command.user_id} not found.")
            raise WebServiceError(
                title="User Not Found",
                description="The requested user could not be found.",
                user_message="User not found. Please verify the ID and try again.",
                error_category_type="NOT_FOUND_ERROR",
                error_code=status.HTTP_404_NOT_FOUND,
                kwargs={"command": command},
            )
        else:
            user_data = self._to_user_representation(user, command)
            return UserResponseModel(
                data=user_data, message="User successfully fetched!"
            )

    @db.transactional()
    async def update_user(
        self, command: UpdateUserCommand
    ) -> UserResponseModel:
        try:
            _update_user_data = command.attributes.model_dump()
            logger.debug(f"Update data received: {_update_user_data}")
            _update_user_data.pop("id", None)
            _password = _update_user_data.pop("password", None)
            if _password is not None:
                logger.debug("Hashing new password for the user.")
                salt = bcrypt.gensalt()
                _update_user_data["password_salt"] = salt
                _update_user_data["hashed_password"] = hash_password(
                    _password, salt
                )

            res = await self.user_repository.update_by_id(
                command.user_id, _update_user_data
            )
            logger.info(f"User with ID {command.user_id} successfully updated.")
            user_data = self._to_user_representation(res, command)
            return UserResponseModel(
                data=user_data, message="User successfully updated!"
            )
        except Exception as e:
            logger.error(e)
            raise e

    @db.transactional()
    async def delete_user(self, command: DeleteUserCommand) -> Any:
        logger.info(f"Attempting to delete user with ID: {command.user_id}")
        try:
            res = await self.user_repository.delete_by_id(command.user_id)
            logger.debug(f"Delete operation result: {res}")
        except Exception as e:
            logger.error(f"Error during deletion of user with ID {command.user_id}: {e}")
            raise WebServiceError(
                error_message="The user with the specified ID does not exist. Deletion failed.",
                error_code=status.HTTP_404_NOT_FOUND,
                is_public=True
            ) from e
        else:
            user_data = self._to_user_representation(res, command)
            logger.info(f"User with ID {command.user_id} deleted successfully.")
            return UserResponseModel(
                data=user_data, message="User successfully deleted!"
            )

    async def get_many_users(
        self, command: GetManyUsersCommand
    ) -> UsersResponseModel:

        logger.info(f"Fetching users with query parameters: {command.query_params}")

        try:
            users, total = await self.user_repository.get_many(
                **command.query_params.model_dump()
            )

            logger.debug(f"Retrieved {len(users)} users with total count {total}.")

        except Exception as e:
            logger.error(f"Error during fetching users: {e}")
            raise e

        if not users:
            logger.warning(
                f"No users found for the provided query parameters: {command.query_params}"
            )

        # users_data = [
        #     self._to_user_representation(user, command) for user in users
        # ]
        # model = user_views.get(command.view_type)
        users_data = TypeAdapter(list[command.get_view_model()]).validate_python(users)


        return UsersResponseModel(
            data=users_data,
            message="Users successfully fetched!",
            metadata={
                "pagination": {
                    "page": command.query_params.offset
                    // command.query_params.limit,
                    "page_size": command.query_params.limit,
                    "total": total,
                }
            },
        )



    def _to_user_representation(
        self, user: Any, command: BaseUserWebCommand
    ) -> BaseUserViewModel:
        logger.debug(f"Converting user to representation with view type: {command.view_type}")
        return command.get_view_model().model_validate(user)

        # model = user_views.get(command.view_type)
        # if not model:
        #     logger.error(f"Invalid user model view type: {command.view_type}")
        #     raise WebServiceError(
        #         error_message=f"Invalid user model view type: {command.view_type}",
        #         error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #     )
        # return model.model_validate(user)


    # def _to_users_representation(
    #     self, users: Any, command: BaseUserWebCommand
    # ) -> Sequence[BaseUserViewModel]:
    #     logger.debug(f"Converting user to representation with view type: {command.view_type}")
    #     model = user_views.get(command.view_type)
    #     if not model:
    #         logger.error(f"Invalid user model view type: {command.view_type}")
    #         raise WebServiceError(
    #             error_message=f"Invalid user model view type: {command.view_type}",
    #             error_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         )
    #     model = user_views.get(command.view_type)
    #     users_data = TypeAdapter(Sequence[model]).validate_python(users)
    #     return users_data




