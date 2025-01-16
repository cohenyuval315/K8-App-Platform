from datetime import datetime

from ..base_schema import BaseSchema
from pydantic import Field


class UpdatedAtSchema(BaseSchema):
    updated_at: datetime = Field(
        ...,
        title=" updated at id",
        description="Timestamp when the object was last updated.",
    )
