from pymicroservicesbase.sdk.web_api.common.configuration.application.commands.get_configuration_command import (
    GetConfigurationCommand,
)
from pymicroservicesbase.sdk.web_api.common.configuration.application.commands.get_configurations_command import (
    GetConfigurationsCommand,
)
from pymicroservicesbase.sdk.web_api.common.configuration.application.commands.update_configurations_command import (
    UpdateConfigurationsCommand,
)
from pymicroservicesbase.sdk.web_api.common.configuration.application.responses.configuration_response import (
    ConfigurationResponse,
)
from pymicroservicesbase.sdk.web_api.common.configuration.application.responses.configurations_response import (
    ConfigurationsResponse,
)


class ConfigurationService:
    async def get_configuration(
        self, configuration: str, command: GetConfigurationCommand
    ) -> ConfigurationResponse:
        return ConfigurationResponse()

    async def get_configurations(
        self, command: GetConfigurationsCommand
    ) -> ConfigurationsResponse:
        return ConfigurationsResponse()

    async def update_configurations(
        self, command: UpdateConfigurationsCommand
    ) -> ConfigurationsResponse:
        return ConfigurationsResponse()
