from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class HealthCheckResponse(BaseResponseSchema[str]):
    data: str | None = None
