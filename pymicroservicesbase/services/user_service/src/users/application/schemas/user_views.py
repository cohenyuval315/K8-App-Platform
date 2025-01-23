from typing import Dict, Literal, Type

from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.admin_user import (
    AdminUserModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.full_user import (
    FullUserModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.minimal_user import (
    MinimalUserModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.owner_user import (
    OwnerUserModel,
)
from pymicroservicesbase.services.user_service.src.users.application.schemas.views.public_user import (
    PublicUserModel,
)
import enum

class UserViewType(str, enum.Enum):
    ADMIN = "admin"
    FULL = "full"
    OWNER = "owner"
    PUBLIC = "public"
    MINIMAL = "minimal"
    INTERNAL = "internal"


user_views: Dict[UserViewType, Type[BaseUserViewModel]] = {
    UserViewType.ADMIN : AdminUserModel,
    UserViewType.FULL : FullUserModel,
    UserViewType.OWNER : OwnerUserModel,
    UserViewType.PUBLIC : PublicUserModel,
    UserViewType.MINIMAL : MinimalUserModel,
    UserViewType.INTERNAL : MinimalUserModel,
}
