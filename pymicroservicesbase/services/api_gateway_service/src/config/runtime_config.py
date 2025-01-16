from pymicroservicesbase.sdk.web_api.core_api.configuration.base_runtime_config import (
    BaseRuntimeConfig,
)


class RuntimeConfig(BaseRuntimeConfig):
    pass


runtime_config = RuntimeConfig(
    DEBUG=False,  # Enable debug mode (should be False in production)
    DEBUGGER_HOST="127.0.0.1",  # Debugger host address
    DEBUGGER_PORT=5678,  # Port for the debugger (adjust if necessary)
    ENVIRONMENT="development",  # Environment type (e.g., "development", "production")
)
