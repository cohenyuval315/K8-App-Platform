from typing import Annotated

from fastapi import Depends, Header, Path, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import (
    CSRF_TOKEN_HEADER_KEY,
    PRODUCT_HEADER_KEY,
)


class GetUserAuthenticationDataCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
    request: Request
    response: Response
    user_id: str
    product_id: str | None

    csrf_token: str | None


async def get_get_user_authentication_data_command(
    request: Request,
    response: Response,
    user_id: str = Path(...),
    product_id: str | None = Header(default=None, alias=PRODUCT_HEADER_KEY),
    csrf_token: str | None = Header(default=None, alias=CSRF_TOKEN_HEADER_KEY),
    # id_token: str | None = Body(),
    # session_id: str | None = Body(),
    # session_token: str | None = Body(),
    # access_token: str | None = Body(),
    # refresh_token: str | None = Body(),
    # csrf_token: str | None = Body(),
) -> GetUserAuthenticationDataCommand:
    return GetUserAuthenticationDataCommand(
        request=request,
        response=response,
        product_id=product_id,
        csrf_token=csrf_token,
        user_id=user_id,
    )


GetUserAuthenticationDataCommandDep = Annotated[
    GetUserAuthenticationDataCommand,
    Depends(get_get_user_authentication_data_command),
]
