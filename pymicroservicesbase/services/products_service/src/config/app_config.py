from pymicroservicesbase.sdk.web_api.core_api.configuration.base_app_config import (
    BaseAppConfig,
)


class AppConfig(BaseAppConfig):
    # AUTHENTICATION_SERVICE:str
    # AUTHORIZATION_SERVICE:str
    pass


app_config = AppConfig(
    APP_NAME="user service",
    APP_DESCRIPTION="user",
    VERSION="1.0.0",
    SUMMARY="user managment",
)
