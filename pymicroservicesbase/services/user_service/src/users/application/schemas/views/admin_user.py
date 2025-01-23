from pydantic import Field
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user_view import (
    BaseUserViewModel,
)
from datetime import datetime


class AdminUserModel(BaseUserViewModel):
    id: str | None
    first_name: str | None
    last_name: str | None
    username: str | None
    email: str | None
    password: str | None = Field(alias="hashed_password")
    # salt:str | None = Field(alias="password_salt")
    created_at: datetime
    created_by: str | None
    updated_by: str | None
    updated_at: datetime
    last_login: datetime | None
    last_request: datetime | None
    is_deleted: bool
    is_active: bool
