from pymicroservicesbase.sdk.web_api.common.types.identifier_type import (
    IdentifierType,
)
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pydantic import Field


class IdentifierSchema(BaseModel):
    id: IdentifierType = Field(...)
