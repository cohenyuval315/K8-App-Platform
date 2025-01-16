from typing import NotRequired
from typing_extensions import TypedDict

from .response_pagination_schema import ResponsePaginationSchema


class ResponseMetaDataSchema(TypedDict):
    pagination: NotRequired[ResponsePaginationSchema]
