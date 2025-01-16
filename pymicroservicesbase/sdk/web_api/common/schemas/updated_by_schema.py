from pydantic import Field
from ..base_schema import BaseSchema
from ..types.identifier_str import IdentifierStr


class UpdatedBySchema(BaseSchema):
    updated_by: IdentifierStr | None = Field(
        None, title="updator user id", description="last user updated."
    )
