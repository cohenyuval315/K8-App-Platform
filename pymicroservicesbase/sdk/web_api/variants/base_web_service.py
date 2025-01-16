from pymicroservicesbase.sdk.web_api.core_api.web_service import WebService
from pymicroservicesbase.sdk.web_api.variants.full_web_service import (
    BaseWebServiceConfig,
)
from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)
from pymicroservicesbase.sdk.web_api.core_api.lifespan.root_lifespan import (
    _lifespan,
)


def create_base_web_service_container(
    config: BaseWebServiceConfig, lifespan
) -> WebServiceContainer:
    web_service = WebService(
        title=config.app_config.APP_NAME,
        description=config.app_config.APP_DESCRIPTION,
        contact={"name": "Yuval Cohen", "email": "cohenyuval315@gmail.com"},
        license_info={
            "name": "Custom License",
            "url": "https://github.com/cohenyuval315/PyMicroservicesBase/blob/main/LICENSE",
        },
        version=config.app_config.VERSION,
        terms_of_service="https://github.com/cohenyuval315/PyMicroservicesBase/blob/main/TERMS_OF_SERVICE.md",
        summary=config.app_config.SUMMARY,
        docs_url=(
            None
            if config.runtime_config.ENVIRONMENT == "production"
            else config.system_config.DOCS_URL
        ),
        redoc_url=(
            None
            if config.runtime_config.ENVIRONMENT == "production"
            else config.system_config.REDOC_URL
        ),
        openapi_url=(
            None
            if config.runtime_config.ENVIRONMENT == "production"
            else config.system_config.OPENAPI_URL
        ),
        debug=config.system_config.DEBUG,
        lifespan=_lifespan(lifespan),
        root_path=config.system_config.ROOT_PATH,
        # servers=config.system_config.SERVERS
        servers=[],
        root_path_in_servers=True,
        swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    )

    wsc = WebServiceContainer(web_service=web_service, config=config)
    return wsc


# def create_web_service_container(
#     config:BaseWebServiceConfig,
#     lifespan,
#     routers: List[WebRouter] | None = None,
#     enable_prometheus: bool = True,
#     health_checks: Dict[str,Callable] | None = {}
# ) -> WebServiceContainer:
#     # Routes
#     wsc = create_base_web_service_container(config,lifespan)
#     web_service = wsc.get_web_service()

#     root_router = WebRouter()
#     root_router.include_router(admin_router)
#     root_router.include_router(status_router)

#     admin_router.include_router(debugging_router)
#     admin_router.include_router(logging_router)
#     admin_router.include_router(memory_router)
#     admin_router.include_router(profiling_router)

#     root_router.include_router(sse_router)
#     root_router.include_router(websockets_router)
#     root_router.include_router(webhooks_router)

#     admin_router.include_router(health_check_router)
#     admin_router.include_router(configuration_router)

#     if routers is None:
#         routers = []

#     for router in routers:
#         root_router.include_router(router)

#     web_service.include_router(root_router)
#     web_service.include_router(admin_router)


#     # # Middlewares
#     # web_service.add_middleware(ErrorMiddleware)
#     # web_service.add_middleware(RequestContextMiddleware)
#     # web_service.add_middleware(ResponseMiddleware)
#     # web_service.add_middleware(LoggingMiddleware, wsc.logger)

#     web_service.add_middleware(
#         CORSMiddleware,
#         allow_origins=config.system_config.ALLOW_ORIGINS,
#         allow_credentials=config.system_config.ALLOW_CREDS,
#         allow_methods=config.system_config.ALLOW_METHODS,
#         allow_headers=config.system_config.ALLOW_HEADERS,
#     )

#     web_service.add_middleware(
#         SessionMiddleware,
#         config.
#     )
#     web_service.add_middleware(
#         TrustedHostMiddleware,
#         allowed_hosts=config.system_config.ALLOWED_HOSTS
#     )

#     # # Compress responses greater than 1kB with optimal compression level as 5
#     # # with level ranging from 1 to 9 with 1 (fastest, least compression)
#     # # and 9 (slowest, most compression)
#     web_service.add_middleware(
#         GZipMiddleware,
#         minimum_size=1024,
#         compresslevel=5  #1 -9 more compression = slower
#     )

#     if config.runtime_config.ENVIRONMENT == "production":
#         web_service.add_middleware(HTTPSRedirectMiddleware)


#     web_service.add_exception_handler(Exception, CentralErrorHandler.handle_request_error)
#     web_service.add_exception_handler(WebServiceError, CentralErrorHandler.handle_request_error)
#     web_service.add_exception_handler(RequestValidationError, CentralErrorHandler.handle_request_error)
#     web_service.add_exception_handler(StarletteHTTPException, CentralErrorHandler.handle_request_error)

#     # @web_service.exception_handler(Exception)
#     # async def exception_handler(request: Request, exc: Exception):
#     #     return await CentralErrorHandler.handle_error(request, exc)

#     # @web_service.exception_handler(WebServiceError)
#     # async def app_error_exception_handler(request: Request, exc: WebServiceError):
#     #     return await CentralErrorHandler.handle_error(request, exc)

#     # @web_service.exception_handler(RequestValidationError)
#     # async def standard_validation_exception_handler(request: Request, exc: RequestValidationError):
#     #     return await CentralErrorHandler.handle_error(request, exc)

#     # @web_service.exception_handler(StarletteHTTPException)
#     # async def http_exception_handler(request: Request, exc: StarletteHTTPException):
#     #     return await CentralErrorHandler.handle_error(request, exc)
#     WebContext.set_web_context(wsc)
#     return wsc
