from pydantic_settings import BaseSettings, SettingsConfigDict

from .base_app_config import BaseAppConfig
from .base_system_config import BaseSystemConfig
from .base_runtime_config import BaseRuntimeConfig


class BaseWebServiceConfig(BaseSettings):
    model_config = SettingsConfigDict(
        # cli_parse_args=os.getenv("ENABLE_CLI", "false").lower() == "true",
        # cli_parse_args=False,
        # cli_avoid_json=True,
        # cli_use_class_docs_for_group=True,
        # cli_enforce_required=False
    )
    app_config: BaseAppConfig
    system_config: BaseSystemConfig
    runtime_config: BaseRuntimeConfig
    # secrets_config: BaseSecretsConfig
