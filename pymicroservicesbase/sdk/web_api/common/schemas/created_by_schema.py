from pydantic import Field
from ..base_schema import BaseSchema
from ..types.identifier_str import IdentifierStr


class CreatedBySchema(BaseSchema):
    created_by: IdentifierStr | None = Field(
        None, title="creator user id", description="user that created this"
    )
