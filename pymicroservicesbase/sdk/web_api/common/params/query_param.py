from __future__ import annotations
from typing import Generic, List


from pydantic import TypeAdapter
from typing import Sequence, TypeVar
import json

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

T = TypeVar("T")


class QueryParam(BaseModel, Generic[T]):
    @classmethod
    async def get_many(cls, values: str | None) -> Sequence[QueryParam[T]]:
        if values is None:
            return []
        adapter = TypeAdapter(List[cls])
        data = adapter.validate_python(json.loads(values))
        return data

    @classmethod
    def get_one(cls, value: str | None) -> QueryParam[T] | None:
        if value is None:
            return None
        adapter = TypeAdapter(cls)
        data = adapter.validate_python(json.loads(value))
        return data
