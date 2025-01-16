from __future__ import annotations
from typing import Annotated, List, Literal, Sequence

from fastapi import Depends
from pydantic import TypeAdapter

from .mapping_param import MappingParam
import json


SortOrderType = Literal[
    "asc",
    "desc",
    1,
    -1,
]


class SortParam(MappingParam[SortOrderType]):
    # sorts:List[str]

    @classmethod
    async def get_many_sorts(
        cls, sorts: str | None = None
    ) -> Sequence[SortParam]:
        if sorts is None:
            return []
        adapter = TypeAdapter(List[SortParam])
        data = adapter.validate_python(sorts)
        return data

    @classmethod
    def get_sort(cls, sort: str | None = None) -> SortParam | None:
        if sort is None:
            return None
        adapter = TypeAdapter(SortParam)
        data = adapter.validate_python(json.loads(sort))
        return data


SortParamsDep = Annotated[List[SortParam], Depends(SortParam.get_many_sorts)]
SortParamDep = Annotated[SortParam, Depends(SortParam.get_sort)]
