from typing import Generic, Sequence, TypeVar

from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pymicroservicesbase.sdk.web_api.core_api.responses.response_metadata_schema import (
    ResponseMetaDataSchema,
)

T = TypeVar("T")


class BaseResponseSchema(BaseModel, Generic[T]):
    model_config: ConfigDict = ConfigDict(
        extra="forbid",
        use_enum_values=True,
    )

    data: T | None = None
    message: Sequence[str] | str | None = None
    metadata: ResponseMetaDataSchema | None = None
