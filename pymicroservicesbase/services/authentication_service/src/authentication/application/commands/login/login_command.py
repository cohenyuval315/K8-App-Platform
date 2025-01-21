from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Annotated, Dict

from fastapi import Body, Depends, Header, Query, Request, Response
from fastapi.security import OAuth2PasswordBearer
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.login_responses import (
    LoginResponseModel,
)
from pymicroservicesbase.shared.constants.headers import PRODUCT_HEADER_KEY

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    auto_error=False,
    description="Login using oauth2 credentials",
    scheme_name="OAuth2 Login Method",
    scopes={},
)


class LoginMethod(ABC):
    @classmethod
    @abstractmethod
    async def _login(cls, method: LoginMethod) -> LoginResponseModel:
        pass


# class MobileLoginMethod(LoginMethod, BaseWebCommand):
#     mobile:str

#     @classmethod
#     async def _login(cls, method: OAuthLoginMethod) -> LoginResponseModel:
#         pass


# class TokenLoginMethod(LoginMethod, BaseWebCommand):
#     token:str

#     @classmethod
#     async def _login(cls, method: OAuthLoginMethod) -> LoginResponseModel:
#         pass


# class OAuthLoginMethod(LoginMethod, BaseWebCommand):
#     model_config:ConfigDict = ConfigDict(
#         arbitrary_types_allowed=True
#     )
#     grant_type:str | None = None
#     username:str
#     password: str
#     scope:str = ""
#     client_id:str | None = None
#     client_secret:str | None = None

#     @classmethod
#     async def _login(cls, method: OAuthLoginMethod) -> LoginResponseModel:
#         pass


# async def get_mobile_login_method(
#     mobile: str | None = Body(default=None, embed=True),
# ):
#     if mobile is not None:
#         return MobileLoginMethod(mobile=mobile)
#     return None

# async def get_oauth_scheme(

# ):
#     oauth2_scheme = OAuth2PasswordBearer(
#         tokenUrl="token",
#         auto_error=False,
#         description= "Login using oauth2 credentials",
#         scheme_name="OAuth2 Login Method",
#         scopes={}
#     )
#     return Depends(oauth2_scheme)


# async def get_token_login_method(
#     token:str | None = Depends(oauth2_scheme),
# ):
#     if token is not None:
#         return TokenLoginMethod(token=token)
#     return None

# async def get_oauth_login_method(
#     grant_type:str | None = Body(),
#     username:str | None = Body(),
#     password: str | None =Body(),
#     scope:str = Body(),
#     client_id:str | None = Body(),
#     client_secret:str | None = Body(),
# ):
#     if username is None or password is None:
#         return None

#     return OAuthLoginMethod(
#         client_id=client_id,
#         client_secret=client_secret,
#         grant_type=grant_type,
#         scope=scope,
#         password=password,
#         username=username
#     )


# MobileLoginMethodDep = Annotated[MobileLoginMethod | None, Depends(get_mobile_login_method)]
# TokenLoginMethodDep = Annotated[TokenLoginMethod | None, Depends(get_token_login_method)]
# OAuthLoginMethodDep = Annotated[OAuthLoginMethod | None, Depends(get_oauth_login_method)]

# LoginMethodType = Union[OAuthLoginMethod,TokenLoginMethod,MobileLoginMethod]


# async def get_login_method(
#     oauth_login_method: OAuthLoginMethodDep,
#     token_login_method: TokenLoginMethodDep,
#     mobile_login_method: MobileLoginMethodDep,
# ) -> LoginMethod | None:
#     if token_login_method is not None:
#         return token_login_method

#     if oauth_login_method is not None:
#         return oauth_login_method

#     if mobile_login_method is not None:
#         return mobile_login_method


class LoginCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(
        arbitrary_types_allowed=True,
        use_enum_values=True,
    )
    login_method: str
    # product: Dict[str, Any]
    provider: str | None
    response: Response
    request: Request
    product_id: str
    data: dict


async def get_login_command(
    # login_method: Annotated[LoginMethod | None ,Depends(get_login_method)],
    response: Response,
    request: Request,
    # product: Dict[str, Any] = Body(embed=True),
    login_method: str = Query(default="password"),
    product_id: str = Header(default="test", alias=PRODUCT_HEADER_KEY),
    provider: str | None = Query(default=None),
    data: dict[str, str] = Body(
        ..., examples=[{"username": "test", "password": "test"}]
    ),
):
    command = LoginCommand(
        login_method=login_method,
        response=response,
        provider=provider,
        request=request,
        # product=product,
        product_id=product_id,
        data=data,
    )
    return command


LoginCommandDep = Annotated[LoginCommand, Depends(get_login_command)]
