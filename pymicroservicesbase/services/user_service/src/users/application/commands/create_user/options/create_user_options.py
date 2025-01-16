from typing import Union

from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.v1 import (
    CreateUserVersionOne,
)
from pymicroservicesbase.services.user_service.src.users.application.commands.create_user.options.v2 import (
    CreateUserVersionTwo,
)


CreateUserOptions = Union[CreateUserVersionOne, CreateUserVersionTwo]
