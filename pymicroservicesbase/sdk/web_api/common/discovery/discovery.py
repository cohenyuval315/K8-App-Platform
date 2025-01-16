from typing import Annotated, Any, Dict

from fastapi import Depends, Header, Path

from pymicroservicesbase.sdk.discovery.product_discovery_service import (
    ProductDiscoveryService,
)
from pymicroservicesbase.sdk.discovery.service_discovery_service import (
    ServiceDiscoveryService,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.api_gateway_service.logger import logger
from pymicroservicesbase.shared.constants.headers import PRODUCT_HEADER_KEY


async def get_service_discovery_service() -> ServiceDiscoveryService:
    service = ServiceDiscoveryService()
    return service


async def get_product_discovery_service() -> ProductDiscoveryService:
    service = ProductDiscoveryService()
    return service


ProductDiscoveryServiceDep = Annotated[
    ProductDiscoveryService, Depends(get_product_discovery_service)
]
ServiceDiscoveryServiceDep = Annotated[
    ServiceDiscoveryService, Depends(get_service_discovery_service)
]


async def get_valid_service_url(
    service_discovery: ServiceDiscoveryService = Depends(
        get_service_discovery_service
    ),
    path: str = Path(...),
):
    logger.info(path)
    if path is None:
        raise WebServiceError(
            title="path cannot be None",
            description="path is missing",
            error_code=400,
            error_severity="MEDIUM_LIMITED",
        )
    try:
        service_url = service_discovery.get_service_url(path)
        logger.debug(f"service url {service_url}")
        url = f"{service_url}/{path}"
        return url

    except KeyError as e:
        raise WebServiceError(
            title="invalid service key",
            description=f"path '{path}' does not lead to any service",
            error_code=400,
            user_message="dont even try",
            error_severity="MEDIUM_LIMITED",
        ) from e
    except (TypeError, ValueError, AttributeError, IndexError) as e:
        raise WebServiceError(
            title="invalid path",
            description=f"path '{path}' is not a valid string",
            error_code=500,
            error_category_type="DEVELOPER_ERROR",
            error_severity="HIGH_MAJOR_ISSUE",
        ) from e


# def get_product_id(value: str = Header(..., alias=PRODUCT_ID_HEADER_KEY)):
#     # Replace "expected_value" with the value you are checking for
#     if value != "expected_value":
#         raise HTTPException(status_code=400, detail="Invalid header value")
#     return value


async def get_valid_product_config(
    product_discovery: ProductDiscoveryService = Depends(
        get_product_discovery_service
    ),
    x_product_id: str = Header(alias=PRODUCT_HEADER_KEY),
) -> Dict[str, Any]:
    try:
        product = product_discovery.get_product_config_by_key(x_product_id)
        return product

    except KeyError as e:
        raise WebServiceError(
            title=f"invalid product ID {x_product_id}",
            description=f"product '{x_product_id}' does not exists",
            error_code=400,
            user_message="dont even try",
        ) from e


ServiceUrlDep = Annotated[str, Depends(get_valid_service_url)]
ProductConfigDep = Annotated[Dict[str, Any], Depends(get_valid_product_config)]
