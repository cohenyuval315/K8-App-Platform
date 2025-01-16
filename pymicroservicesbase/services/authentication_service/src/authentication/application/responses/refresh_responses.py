from typing import Any

from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class RefreshResponseModel(BaseResponseSchema[Any]):
    data: Any | None | Any = None
