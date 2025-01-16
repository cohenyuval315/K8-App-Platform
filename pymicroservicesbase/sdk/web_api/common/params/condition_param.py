from __future__ import annotations

from typing import Annotated, List, TypeVar, Generic

from fastapi import Depends

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel

from .query_param import QueryParam

T = TypeVar("T")
K = TypeVar("K")


class ConditionParam(QueryParam[T], BaseModel, Generic[T, K]):
    field: str
    value: T
    operator: K
    regex: bool = False


ConditionParamsDep = Annotated[
    List[ConditionParam], Depends(ConditionParam.get_many)
]

ConditionParamDep = Annotated[ConditionParam, Depends(ConditionParam.get_one)]
