from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.run_health_checks_command import (
    RunHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_check_command import (
    GetHealthCheckCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.commands.get_health_checks_command import (
    GetHealthChecksCommand,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_check_response import (
    HealthCheckResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_response import (
    HealthChecksResponse,
)
from pymicroservicesbase.sdk.web_api.common.health_check.application.responses.health_checks_status_response import (
    HealthChecksStatusResponse,
)


class HealthCheckService:
    def __init__(self, available_health_checks, all_health_checks):
        pass

    def get_health_check(
        self, command: GetHealthCheckCommand
    ) -> HealthCheckResponse:
        pass

    def get_health_checks(
        self, command: GetHealthChecksCommand
    ) -> HealthChecksResponse:
        pass

    def run_health_checks(
        self, command: RunHealthChecksCommand
    ) -> HealthChecksStatusResponse:
        pass
        # health_check_tasks = []
        # health_checks = get_health_checks_from_string(health_checks)
        # for health_check in health_checks:
        #     if health_check not in  health_checks:
        #         raise HealthCheckDoesNotExistsError(health_check)
        #     else:
        #         health_check_tasks.append(health_checks[health_check].run_test())
        # try:
        #     results = await asyncio.gather(*health_check_tasks,return_exceptions=True)
        #     return results
        # except WebServiceErrors as e:
        #     raise e
        # finally:
        #     return
