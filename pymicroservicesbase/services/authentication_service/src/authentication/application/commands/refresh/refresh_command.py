from typing import Annotated

from fastapi import Depends, Header, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import PRODUCT_HEADER_KEY


class RefreshCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
    request: Request
    response: Response
    product_id: str

    refresh_session: bool
    refresh_csrf_token: bool
    refresh_session_id_token: bool
    refresh_session_token: bool
    refresh_access_token: bool


async def get_refresh_command(
    request: Request,
    response: Response,
    product_id: str = Header(default=None, alias=PRODUCT_HEADER_KEY),
    refresh_session: bool = Header(default=False, alias=None),
    refresh_csrf_token: bool = Header(default=False, alias=None),
    refresh_session_id_token: bool = Header(default=False, alias=None),
    refresh_session_token: bool = Header(default=False, alias=None),
    refresh_access_token: bool = Header(default=False, alias=None),
    # id_token: str | None = Body(),
    # session_id: str | None = Body(),
    # session_token: str | None = Body(),
    # access_token: str | None = Body(),
    # refresh_token: str | None = Body(),
    # csrf_token: str | None = Body(),
) -> RefreshCommand:
    return RefreshCommand(
        request=request,
        response=response,
        product_id=product_id,
        refresh_session=refresh_session,
        refresh_csrf_token=refresh_csrf_token,
        refresh_session_id_token=refresh_session_id_token,
        refresh_session_token=refresh_session_token,
        refresh_access_token=refresh_access_token,
    )


RefreshCommandDep = Annotated[RefreshCommand, Depends(get_refresh_command)]
