from typing import List

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pymicroservicesbase.services.user_service.src.users.application.schemas.base_user import (
    BaseUserModel,
)


class BaseUsersModel(BaseModel):
    data: List[BaseUserModel]


# class UserSchema(ObjectIdSchema,UserFullNamesModificationSchema,ModificationTimestampSchema,UserIdentifiersModificationSchema):
#     email : EmailStr = Field(None, title="Email", description="User email address")
#     username : UserNameStr = Field(None, title="Username", description="User's username")
#     first_name : Optional[NameStr] = Field(None, title="First Name", description="User's first name")
#     last_name : Optional[NameStr] = Field(None, title="Last Name", description="User's last name")
#     last_login: Optional[date] = Field(None, title="last_login", description="Any additional user data")


# class PublicUserSchema(ObjectIdSchema,UserFullNamesModificationSchema,ModificationTimestampSchema):
#     email: EmailStr = Field(..., title="Email", description="User email address")
#     first_name: Optional[NameStr] = Field(None, title="First Name", description="User's first name")
#     last_name : Optional[NameStr]= Field(None, title="Last Name", description="User's last name")
#     last_login: Optional[date] = Field(None, title="last_login", description="Any additional user data")


# class UserCreateSchema(BaseSchema):
#     email :EmailStr = Field(..., title="Email", description="User email address")
#     username : UserNameStr = Field(..., title="Username", description="User's username")
#     password : PassWordStr = Field(..., title="Password", description="Password",repr=False)
#     first_name : NameStr = Field(None, title="First Name", description="User's first name")
#     last_name : NameStr = Field(None, title="LaBaseUserSchema,Creast Name", description="User's last name")

# class UserUpdateSchema(BaseSchema):
#     email : Optional[EmailStr] = Field(None, title="Email", description="User email address")
#     username : Optional[UserNameStr]= Field(None, title="Username", description="User's username")
#     password : Optional[PassWordStr] = Field(None, title="Password", description="Password",repr=False)
#     first_name : Optional[NameStr] = Field(None, title="First Name", description="User's first name")
#     last_name : Optional[NameStr] = Field(None, title="First Name", description="User's Last name")

# class UserResponseSchema(BaseResponseSchemaSchema):
#     data: UserSchema

# class UsersResponseSchema(BaseResponseSchemaSchema):
#     data: List[UserSchema]

# class PublicUserResponseSchema(BaseResponseSchemaSchema):
#     data: PublicUserSchema

# class PublicUsersResponseSchema(BaseResponseSchemaSchema):
#     data: List[PublicUserSchema]


# class UserRoleSchema(BaseModel):
#     role_id : Annotated[
#                     Optional[str],
#                     StringConstraints(
#                         strip_whitespace=True,
#                         to_upper=None,
#                         to_lower=None,
#                         strict=None,
#                         max_length=None,
#                         min_length=None,
#                         pattern=None,
#                     ),
#                 ] = Field(None, title="Role ID", description="Unique identifier for the role")

#     role_name : Annotated[
#                     Optional[str],
#                     StringConstraints(
#                         strip_whitespace=True,
#                         to_upper=None,
#                         to_lower=None,
#                         strict=None,
#                         max_length=None,
#                         min_length=None,
#                         pattern=None,
#                     ),
#                 ] = Field(None, title="Role Name", description="Name of the role")


# class UserAccessControlSchema(BaseModel):
#     roles : Annotated[
#                     Optional[List[UserRoleSchema]],
#                     StringConstraints(
#                         strip_whitespace=True,
#                         to_upper=None,
#                         to_lower=None,
#                         strict=None,
#                         max_length=None,
#                         min_length=None,
#                         pattern=None,
#                     ),
#                 ] = Field(None, title="Roles", description="List of roles assigned to the user")
