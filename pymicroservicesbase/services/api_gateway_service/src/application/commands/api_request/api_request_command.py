from typing import Annotated, Any, Dict

from fastapi import Depends, Header, Path, Request, Response
from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.common.discovery.discovery import (
    get_valid_product_config,
    get_valid_service_url,
)
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)
from pymicroservicesbase.shared.constants.headers import PRODUCT_HEADER_KEY


class ApiRequestCommand(BaseWebCommand):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    path: str
    request: Request
    response: Response
    service_url: str
    product_config: Dict[str, Any]
    x_product_key: str


async def get_api_request(
    request: Request,
    response: Response,
    service_url: str = Depends(get_valid_service_url),
    x_product_key: str = Header(alias=PRODUCT_HEADER_KEY),
    product_config: Dict[str, Any] = Depends(get_valid_product_config),
    path: str = Path(...),
) -> ApiRequestCommand:
    _api_request = ApiRequestCommand(
        request=request,
        response=response,
        service_url=service_url,
        product_config=product_config,
        path=path,
        x_product_key=x_product_key,
    )
    return _api_request


ApiRequestCommandDep = Annotated[ApiRequestCommand, Depends(get_api_request)]
