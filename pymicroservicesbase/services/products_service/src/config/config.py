from .app_config import app_config
from .system_config import system_config
from .runtime_config import runtime_config

from pymicroservicesbase.sdk.web_api.core_api.configuration.base_web_service_config import (
    BaseWebServiceConfig,
)


class WebServiceConfig(BaseWebServiceConfig):
    pass


config = WebServiceConfig(
    app_config=app_config,
    system_config=system_config,
    runtime_config=runtime_config,
)
