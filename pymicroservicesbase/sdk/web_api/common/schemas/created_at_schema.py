from datetime import datetime

from ..base_schema import BaseSchema
from pydantic import Field


class CreatedAtSchema(BaseSchema):
    created_at: datetime = Field(
        ...,
        title=" created at id",
        description="Timestamp when the object was created.",
    )
