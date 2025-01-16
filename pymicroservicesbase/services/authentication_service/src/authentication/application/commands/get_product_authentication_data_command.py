from typing import Annotated

from fastapi import Depends, Header, Path, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import CSRF_TOKEN_HEADER_KEY


class GetProductAuthenticationDataCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
    request: Request
    response: Response
    product_id: str | None
    csrf_token: str | None


async def get_get_product_authentication_data_command(
    request: Request,
    response: Response,
    product_id: str = Path(...),
    csrf_token: str | None = Header(default=None, alias=CSRF_TOKEN_HEADER_KEY),
    # id_token: str | None = Body(),
    # session_id: str | None = Body(),
    # session_token: str | None = Body(),
    # access_token: str | None = Body(),
    # refresh_token: str | None = Body(),
    # csrf_token: str | None = Body(),
) -> GetProductAuthenticationDataCommand:
    return GetProductAuthenticationDataCommand(
        request=request,
        response=response,
        product_id=product_id,
        csrf_token=csrf_token,
    )


GetProductAuthenticationDataCommandDep = Annotated[
    GetProductAuthenticationDataCommand,
    Depends(get_get_product_authentication_data_command),
]


GetProductAuthenticationDataCommandDep = Annotated[
    GetProductAuthenticationDataCommand,
    Depends(get_get_product_authentication_data_command),
]
