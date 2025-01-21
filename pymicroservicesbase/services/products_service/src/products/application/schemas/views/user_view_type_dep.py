from typing import Annotated

from fastapi import Query

from pymicroservicesbase.services.user_service.src.users.application.schemas.views.user_views import (
    UserViewType,
)


UserViewTypeDep = Annotated[UserViewType, Query(default="minimal")]
