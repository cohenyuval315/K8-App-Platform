from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)
from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.web_context import WebContext


WebServiceContainerDep = Annotated[
    WebServiceContainer, Depends(WebContext.get_web_context)
]


def get_web_service(
    web_service_container: WebServiceContainerDep,
) -> WebService:
    return web_service_container.get_web_service()


WebServiceDep = Annotated[WebService, Depends(get_web_service)]
