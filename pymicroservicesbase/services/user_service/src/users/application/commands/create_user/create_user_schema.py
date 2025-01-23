from typing import Self
from pydantic import ConfigDict, EmailStr, Field, field_validator,model_validator
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class BaseCreateUserSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

class CreateUserSchema(BaseCreateUserSchema):
    username: str = Field(..., min_length=4, title="username")
    password: str = Field(..., min_length=4, title="password")
    first_name: str | None = Field(default=None, min_length=1, title="first_name")
    last_name: str | None = Field(default=None, min_length=1, title="last_name")
    email: EmailStr


    @field_validator('first_name', 'last_name', mode='before')
    @classmethod
    def capitalize(cls, value: str | None) -> str | None:
        if value is not None:
            return value.capitalize()
        return value


    # @model_validator(mode='after')
    # def post_init_username_email_set(self) -> Self:
    #     if isinstance(self.username, EmailStr) and self.email is None:
    #         self.email = self.username
    #     return self
