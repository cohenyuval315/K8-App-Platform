from typing import Annotated

from fastapi import Depends
from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class AccountRecoveryCommand(BaseWebCommand):
    pass


async def get_account_recovery_command():
    return AccountRecoveryCommand()


AccountRecoveryCommandDep = Annotated[
    AccountRecoveryCommand, Depends(get_account_recovery_command)
]
