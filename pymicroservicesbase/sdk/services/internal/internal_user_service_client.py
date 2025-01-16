import json
from typing import Any

from pymicroservicesbase.sdk.services.internal.internal_service_client import (
    InternalServiceClient,
)


class InternalUserServiceClient(InternalServiceClient):
    def __init__(
        self,
        host: str = "users",
        port: int = 8002,
        prefix: str = "users",
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(host=host, port=port, prefix=prefix, *args, **kwargs)

    async def create_user(self, data: dict, params: dict, *args, **kwargs):
        response = await self.client.post(
            f"/{self.prefix}", json=data, params=params, *args, **kwargs
        )
        return response

    async def get_user(self, user_id: str, *args, **kwargs):
        response = await self.client.get(
            f"/{self.prefix}/{user_id}",
            params={"view_type": "admin"},
            *args,
            **kwargs,
        )
        return response

    async def get_users(self, filters, *args, **kwargs):
        response = await self.client.get(
            f"/{self.prefix}/",
            params={
                "offset": 0,
                "limit": 1,
                "filters": json.dumps(filters),
                "view_type": "admin",
            },
            *args,
            **kwargs,
        )
        return response
