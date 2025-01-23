from typing import Optional

from pydantic import ConfigDict, EmailStr, Field

from pymicroservicesbase.sdk.web_api.common.schemas.identifier_schema import (
    IdentifierSchema,
)
from pymicroservicesbase.sdk.web_api.common.types.letters_only_type import (
    LettersOnlyType,
)
from pymicroservicesbase.sdk.web_api.common.types.username_type import (
    UserNameStrType,
)
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class UserSchema(IdentifierSchema, BaseModel):
    email: EmailStr | None = Field(...)
    username: UserNameStrType | None = Field(
        None, title="Username", description="User's username"
    )
    first_name: Optional[LettersOnlyType] = Field(
        None, title="First Name", description="User's first name"
    )
    last_name: Optional[LettersOnlyType] = Field(
        None, title="Last Name", description="User's last name"
    )


class BaseUserViewModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
