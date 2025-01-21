from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.services.user_service.src.database.session_dep import (
    SessionDep,
)
from pymicroservicesbase.services.user_service.src.users.api.controllers.user_controller import (
    UserController,
)
from pymicroservicesbase.services.user_service.src.users.domain.services.user_service import (
    UserService,
)
from pymicroservicesbase.services.user_service.src.database.repositories.user_repository import (
    UserRepository,
)


def get_user_controller(db_session: SessionDep) -> UserController:
    return UserController(UserService(UserRepository(db_session)))


UserControllerDep = Annotated[UserController, Depends(get_user_controller)]
