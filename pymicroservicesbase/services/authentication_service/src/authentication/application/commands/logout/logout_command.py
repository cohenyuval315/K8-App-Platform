from typing import Annotated

from fastapi import Depends, Header, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import PRODUCT_HEADER_KEY


class LogoutCommand(BaseWebCommand):
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
    request: Request
    response: Response
    product_id: str
    # id_token: str | None = None
    # session_id: str | None = None
    # session_token: str | None = None
    # access_token: str | None = None
    # refresh_token: str | None = None
    # csrf_token: str | None = None


async def get_logout_command(
    request: Request,
    response: Response,
    # id_token: str | None = Body(),
    # session_id: str | None = Body(),
    # session_token: str | None = Body(),
    # access_token: str | None = Body(),
    # refresh_token: str | None = Body(),
    # csrf_token: str | None = Body(),
    product_id: str = Header(default=None, alias=PRODUCT_HEADER_KEY),
) -> LogoutCommand:
    return LogoutCommand(
        request=request,
        response=response,
        product_id=product_id,
        # id_token=id_token,
        # session_id=session_id,
        # session_token=session_token,
        # access_token=access_token,
        # refresh_token=refresh_token,
        # csrf_token=csrf_token,
    )


LogoutCommandDep = Annotated[LogoutCommand, Depends(get_logout_command)]
