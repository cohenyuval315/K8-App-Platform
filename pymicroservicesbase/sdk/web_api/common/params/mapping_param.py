from __future__ import annotations

from typing import Annotated, List, TypeVar

from fastapi import Depends
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

from .query_param import QueryParam

T = TypeVar("T")


class MappingParam(QueryParam[T], BaseModel):
    field: str
    value: T


MappingParamsDep = Annotated[
    List[MappingParam], Depends(MappingParam.get_many)
]
MappingParamDep = Annotated[MappingParam, Depends(MappingParam.get_one)]
