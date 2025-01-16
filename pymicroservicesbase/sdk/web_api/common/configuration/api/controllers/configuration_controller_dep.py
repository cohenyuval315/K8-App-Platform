from typing import Annotated
from fastapi import Depends
from pymicroservicesbase.sdk.web_api.common.configuration.api.controllers.configuration_controller import (
    ConfigurationController,
)
from pymicroservicesbase.sdk.web_api.common.configuration.domain.configuration_service import (
    ConfigurationService,
)


def get_configuration_controller() -> ConfigurationController:
    return ConfigurationController(ConfigurationService())


ConfigurationControllerDep = Annotated[
    ConfigurationController, Depends(get_configuration_controller)
]
