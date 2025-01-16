from pymicroservicesbase.sdk.web_api.common.configuration.domain.configuration_service import (
    ConfigurationService,
)
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


class ConfigurationController:
    def __init__(self, configuration_service: ConfigurationService):
        self.configuration_service = configuration_service

    async def get_configuration(
        self,
        configuration: str,
        command: GetConfigurationCommand,
    ) -> ConfigurationResponse:
        return await self.configuration_service.get_configuration(
            configuration, command
        )

    async def get_configurations(
        self, command: GetConfigurationsCommand
    ) -> ConfigurationsResponse:
        return await self.configuration_service.get_configurations(command)

    async def update_configurations(
        self, command: UpdateConfigurationsCommand
    ) -> ConfigurationsResponse:
        return await self.configuration_service.update_configurations(command)
