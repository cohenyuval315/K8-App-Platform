from .....core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.common.configuration.api.controllers.configuration_controller_dep import (
    ConfigurationControllerDep,
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


configuration_router = WebRouter(
    prefix="/configuration", tags=["configuration"]
)


@configuration_router.get(
    "/{configuration}", response_model=ConfigurationResponse, status_code=200
)
async def get_configuration(
    configuration: str,
    command: GetConfigurationCommand,
    controller: ConfigurationControllerDep,
) -> ConfigurationResponse:
    return await controller.get_configuration(configuration, command)


@configuration_router.get(
    "", response_model=ConfigurationsResponse, status_code=200
)
async def get_configurations(
    command: GetConfigurationsCommand, controller: ConfigurationControllerDep
) -> ConfigurationsResponse:
    return await controller.get_configurations(command)


@configuration_router.put(
    "", response_model=ConfigurationsResponse, status_code=200
)
async def update_configurations(
    command: UpdateConfigurationsCommand,
    controller: ConfigurationControllerDep,
) -> ConfigurationsResponse:
    return await controller.update_configurations(command)
