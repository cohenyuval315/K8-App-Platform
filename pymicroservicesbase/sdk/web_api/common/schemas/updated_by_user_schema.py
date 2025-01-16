from typing import Optional, Union

from ..types.full_name_str import FullNameStr
from ..types.letters_only_str import LettersOnlyStr
from ..base_schema import BaseSchema
from pydantic import Field


class UpdatedByUserSchema(BaseSchema):
    updated_by_user: Optional[Union[LettersOnlyStr, FullNameStr]] = Field(
        None, title="updator user full name", description="ful name of user"
    )
