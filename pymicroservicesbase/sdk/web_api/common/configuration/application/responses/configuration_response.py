from pymicroservicesbase.sdk.web_api.core_api.responses.base_response_schema import (
    BaseResponseSchema,
)


class ConfigurationResponse(BaseResponseSchema[str]):
    data: str | None = None
