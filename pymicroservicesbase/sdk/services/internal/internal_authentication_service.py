from typing import Any
from pymicroservicesbase.sdk.services.internal.internal_service_client import (
    InternalServiceClient,
)


class InternalAuthenticationServiceClient(InternalServiceClient):
    def __init__(
        self,
        host: str = "authentication",
        port: int = 8001,
        prefix: str = "auth",
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(host=host, port=port, prefix=prefix, *args, **kwargs)

    async def verify(self, headers, cookies, *args, **kwargs):
        response = await self.post(
            f"/{self.prefix}/verify",
            headers=headers,
            cookies=cookies,
            *args,
            **kwargs,
        )
        return response
