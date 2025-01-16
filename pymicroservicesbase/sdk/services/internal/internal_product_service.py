from typing import Any

from pymicroservicesbase.sdk.services.internal.internal_service_client import (
    InternalServiceClient,
)


class InternalProductServiceClient(InternalServiceClient):
    def __init__(
        self,
        host: str = "products",
        port: int = 8003,
        prefix: str = "products",
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(host=host, port=port, prefix=prefix, *args, **kwargs)
