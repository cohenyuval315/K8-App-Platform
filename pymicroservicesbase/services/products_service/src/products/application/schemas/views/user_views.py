from typing import Dict, Literal, Type

from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
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


UserViewType = Literal[
    "admin", "full", "owner", "public", "minimal", "internal"
]

user_views: Dict[UserViewType, Type[BaseUserModel]] = {
    "admin": AdminUserModel,
    "full": FullUserModel,
    "owner": OwnerUserModel,
    "public": PublicUserModel,
    "minimal": MinimalUserModel,
    "internal": MinimalUserModel,
}
