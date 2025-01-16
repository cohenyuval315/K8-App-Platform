from pymicroservicesbase.sdk.web_api.core_api.configuration.base_system_config import (
    BaseSystemConfig,
)


class SystemConfig(BaseSystemConfig):
    pass


# system_config = SystemConfig(
#     ALLOW_CREDS=,
#     ALLOW_HEADERS=,
#     ALLOW_METHODS=,
#     ALLOW_ORIGINS=,
#     ALLOWED_HOSTS=,
#     APP_HOST=,
#     APP_PORT=,
#     DEBUG=,
#     DEBUGGER_HOST=,
#     DEBUGGER_PORT=,
#     DOCS_URL=,
#     ENVIRONMENT=,
#     PRINT_APP=,
#     PRINT_ENVIRONMENT=,
#     REDOC_URL=
# )

system_config = SystemConfig(
    ALLOW_CREDS=True,  # Allow credentials in CORS requests
    # ALLOW_HEADERS=["Content-Type", "Authorization", "X-Requested-With"],  # Allowed headers in CORS
    ALLOW_HEADERS=["*"],
    ALLOW_METHODS=["*"],  # Allowed methods in CORS
    ALLOW_ORIGINS=[
        "http://localhost:3000"
    ],  # Allow all origins for CORS (adjust for production)
    # ALLOW_ORIGINS=["*"],  # Allow all origins for CORS (adjust for production)
    # ALLOWED_HOSTS=["localhost", "127.0.0.1"],  # Hosts allowed to connect to the application
    ALLOWED_HOSTS=["*"],  # Hosts allowed to connect to the application
    APP_HOST="0.0.0.0",  # Application host address
    APP_PORT=8000,  # Port where the app will listen
    DEBUG=False,  # Enable debug mode (should be False in production)
    DEBUGGER_HOST="127.0.0.1",  # Debugger host address
    DEBUGGER_PORT=5678,  # Port for the debugger (adjust if necessary)
    ENVIRONMENT="development",  # Environment type (e.g., "development", "production")
    PRINT_APP=True,  # Whether to print application start info
    PRINT_ENVIRONMENT=True,  # Whether to print environment-related info
    DOCS_URL="/docs",  # URL endpoint for the Swagger UI documentation
    REDOC_URL="/redoc",  # URL endpoint for the ReDoc documentation
    OPENAPI_URL="/openapi.json",
    ROOT_PATH="/api",
)
