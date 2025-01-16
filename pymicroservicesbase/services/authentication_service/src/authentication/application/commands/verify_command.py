from typing import Annotated

from fastapi import Depends, Header, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import (
    CSRF_TOKEN_HEADER_KEY,
    PRODUCT_HEADER_KEY,
    VERIFY_ACCESS_TOKEN_HEADER_KEY,
    VERIFY_CSRF_TOKEN_HEADER_KEY,
    VERIFY_REFRESH_TOKEN_HEADER_KEY,
    VERIFY_SESSION_ID_TOKEN_KEY_HEADER_KEY,
    VERIFY_SESSION_TOKEN_HEADER_KEY,
)


class VerifyCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
    request: Request
    response: Response
    product_id: str | None
    csrf_token: str | None

    verify_csrf_token: bool
    verify_session_id_token: bool
    verify_session_token: bool
    verify_access_token: bool
    verify_refresh_token: bool


async def get_verify_command(
    request: Request,
    response: Response,
    product_id: str | None = Header(default=None, alias=PRODUCT_HEADER_KEY),
    csrf_token: str | None = Header(default=None, alias=CSRF_TOKEN_HEADER_KEY),
    verify_csrf_token: bool = Header(
        default=True, alias=VERIFY_CSRF_TOKEN_HEADER_KEY
    ),
    verify_session_id_token: bool = Header(
        default=True, alias=VERIFY_SESSION_ID_TOKEN_KEY_HEADER_KEY
    ),
    verify_session_token: bool = Header(
        default=False, alias=VERIFY_SESSION_TOKEN_HEADER_KEY
    ),
    verify_access_token: bool = Header(
        default=False, alias=VERIFY_ACCESS_TOKEN_HEADER_KEY
    ),
    verify_refresh_token: bool = Header(
        default=False, alias=VERIFY_REFRESH_TOKEN_HEADER_KEY
    ),
) -> VerifyCommand:
    return VerifyCommand(
        request=request,
        response=response,
        product_id=product_id,
        csrf_token=csrf_token,
        verify_csrf_token=verify_csrf_token,
        verify_session_id_token=verify_session_id_token,
        verify_session_token=verify_session_token,
        verify_access_token=verify_access_token,
        verify_refresh_token=verify_refresh_token,
    )


VerifyCommandDep = Annotated[VerifyCommand, Depends(get_verify_command)]
