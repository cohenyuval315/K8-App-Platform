from contextlib import asynccontextmanager

from pymicroservicesbase.sdk.services.internal.internal_authentication_service import (
    InternalAuthenticationServiceClient,
)
from pymicroservicesbase.sdk.web_api.common.requests.request_purge_headers_middleware import (
    RequestPurgeHeadersMiddleware,
)
from pymicroservicesbase.sdk.web_api.common.responses.response_purge_headers_middleware import (
    ResponsePurgeHeadersMiddleware,
)
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.logging.web_service_logger import (
    WebServiceLogger,
)
from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)
from pymicroservicesbase.sdk.web_api.variants.full_web_service import (
    ForwardHeadersMiddleware,
    create_web_service_container,
)
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.api.routes.api_gateway_router import (
    api_gateway_router,
)
from pymicroservicesbase.services.api_gateway_service.src.api_gateway.domain.services.proxy_client import (
    ProxyClient,
)
from pymicroservicesbase.services.api_gateway_service.src.config.config import (
    config,
)
from pymicroservicesbase.services.api_gateway_service.src.middlewares.authentication_middleware import (
    AuthenticationMiddleware,
)
from pymicroservicesbase.services.api_gateway_service.src.middlewares.correlation_id_middleware import (
    CorrelationIdMiddleware,
)
from pymicroservicesbase.services.api_gateway_service.src.middlewares.redirects_middleware import (
    RedirectsMiddleware,
)
from pymicroservicesbase.services.api_gateway_service.src.middlewares.request_private_path_middleware import (
    RequestPrivatePathMiddleware,
)
from pymicroservicesbase.shared.constants.headers import (
    ACCESS_TOKEN_HEADER_KEY,
    CONTENT_ENCODING_HEADER_KEY,
    CONTENT_LANGUAGE_HEADER_KEY,
    CONTENT_LENGTH_HEADER_KEY,
    CONTENT_TYPE_HEADER_KEY,
    CONTENT_TYPE_OPTIONS_HEADER_KEY,
    COOKIE_HEADER_KEY,
    CORRELATION_ID_HEADER_KEY,
    CSRF_TOKEN_HEADER_KEY,
    DATE_HEADER_KEY,
    FRAME_OPTIONS_HEADER_KEY,
    HOST_HEADER_KEY,
    LOCATION_HEADER_KEY,
    PRODUCT_HEADER_KEY,
    PRODUCT_ID_HEADER_KEY,
    PRODUCT_NAME_HEADER_KEY,
    REFRESH_TOKEN_HEADER_KEY,
    REQUEST_ID_HEADER_KEY,
    RETRY_AFTER_HEADER_KEY,
    SERVER_HEADER_KEY,
    SERVICE_ID_HEADER_KEY,
    SERVICE_NAME_HEADER_KEY,
    SESSION_ID_HEADER_KEY,
    SESSION_TOKEN_HEADER_KEY,
    SET_COOKIE_HEADER_KEY,
    TRANSFER_ENCODING_HEADER_KEY,
    USER_EMAIL_HEADER_KEY,
    USER_ID_HEADER_KEY,
    USER_IDENTIFIER_HEADER_KEY,
    USER_USERNAME_HEADER_KEY,
    VERIFY_ACCESS_TOKEN_HEADER_KEY,
    VERIFY_ACTIVE_SESSION_KEY_HEADER_KEY,
    VERIFY_CSRF_TOKEN_HEADER_KEY,
    VERIFY_REFRESH_TOKEN_HEADER_KEY,
    VERIFY_SESSION_ID_TOKEN_KEY_HEADER_KEY,
    VERIFY_SESSION_TOKEN_HEADER_KEY,
    XSS_PROTECTION_HEADER_KEY,
)


# from pymicroservicesbase.services.api_gateway_service.src.api_gateway.middlewares.request_middleware import RequestMiddleware

# from pymicroservicesbase.services.api_gateway_service.src.api_gateway.middlewares.response_middleware import ResponseHeadersMiddleware
from pymicroservicesbase.sdk.web_api.common.responses.response_with_headers_middleware import (
    ResponseWithHeadersMiddleware,
)
from pymicroservicesbase.services.api_gateway_service.src.errors.api_gateway_web_service_error_handler import (
    APIGatewayWebServiceErrorHandler,
)

from pymicroservicesbase.services.api_gateway_service.logger import logger


@asynccontextmanager
async def lifespan(app: WebService):
    proxy_client = ProxyClient(event_hooks={"request": [], "response": []})
    yield
    await proxy_client.close()


def create_api_gateway_web_service() -> WebServiceContainer:
    web_service_logger = WebServiceLogger(logger=logger)

    auth_client = InternalAuthenticationServiceClient("APIGateway")
    container = create_web_service_container(
        lifespan=lifespan,
        logger=web_service_logger,
        config=config,
        routers=[api_gateway_router],
        with_web_service_error=False,
    )
    web_service = container.get_web_service()

    web_service.add_middleware(RequestPrivatePathMiddleware, ["auth/verify"])
    web_service.add_middleware(CorrelationIdMiddleware)
    web_service.add_middleware(RedirectsMiddleware, {})
    web_service.add_middleware(
        AuthenticationMiddleware,
        auth_client,
        ["docs"],  # exclude_paths
        ["auth"],  # include_paths
    )

    web_service.add_middleware(
        RequestPurgeHeadersMiddleware,
        [
            # CONTENT_LENGTH_HEADER_KEY
        ],
    )
    web_service.add_middleware(
        ResponsePurgeHeadersMiddleware,
        [
            SERVER_HEADER_KEY,
            HOST_HEADER_KEY,
            CONTENT_LENGTH_HEADER_KEY,
            PRODUCT_HEADER_KEY,
            CORRELATION_ID_HEADER_KEY,
            DATE_HEADER_KEY,
            SERVICE_ID_HEADER_KEY,
            SERVICE_NAME_HEADER_KEY,
            USER_EMAIL_HEADER_KEY,
            REQUEST_ID_HEADER_KEY,
            CSRF_TOKEN_HEADER_KEY,
            USER_ID_HEADER_KEY,
            USER_IDENTIFIER_HEADER_KEY,
            USER_USERNAME_HEADER_KEY,
            PRODUCT_ID_HEADER_KEY,
            PRODUCT_NAME_HEADER_KEY,
            SESSION_ID_HEADER_KEY,
            SESSION_TOKEN_HEADER_KEY,
            VERIFY_ACCESS_TOKEN_HEADER_KEY,
            VERIFY_ACTIVE_SESSION_KEY_HEADER_KEY,
            VERIFY_CSRF_TOKEN_HEADER_KEY,
            VERIFY_REFRESH_TOKEN_HEADER_KEY,
            VERIFY_SESSION_ID_TOKEN_KEY_HEADER_KEY,
            VERIFY_SESSION_TOKEN_HEADER_KEY,
            ACCESS_TOKEN_HEADER_KEY,
            REFRESH_TOKEN_HEADER_KEY,
        ],
    )

    web_service.add_middleware(
        ResponseWithHeadersMiddleware,
        [
            (CONTENT_TYPE_OPTIONS_HEADER_KEY, "nosniff"),
            (FRAME_OPTIONS_HEADER_KEY, "DENY"),
            (XSS_PROTECTION_HEADER_KEY, "1; mode=block"),
            # (CONTENT_SECURITY_POLICY_HEADER_KEY, "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; object-src 'none'"),
            # (PERMISSIONS_POLICY_HEADER_KEY, "")
            # (EXPECT_CT_HEADER_KEY, "")
            # (STRICT_TRANSPORT_SECURITY_HEADER_KEY, "max-age=31536000; includeSubDomains; preload")
        ],
    )
    web_service.add_middleware(
        ForwardHeadersMiddleware,
        [
            SET_COOKIE_HEADER_KEY,
            COOKIE_HEADER_KEY,
            RETRY_AFTER_HEADER_KEY,
            LOCATION_HEADER_KEY,
            CONTENT_TYPE_HEADER_KEY,
            CONTENT_ENCODING_HEADER_KEY,
            CONTENT_LANGUAGE_HEADER_KEY,
            TRANSFER_ENCODING_HEADER_KEY,
        ],
    )
    web_service.add_exception_handler(
        WebServiceError, APIGatewayWebServiceErrorHandler().exception_handler
    )  # type: ignore

    return container
