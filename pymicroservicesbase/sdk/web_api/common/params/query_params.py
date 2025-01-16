from typing import Annotated

from fastapi import Depends
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from .sort_param import SortParamsDep
from .filter_param import FilterParamsDep
from .limit_param import LimitParamDep
from .offset_param import OffsetParamDep


# class SortParam(dict):
#     model_config=ConfigDict(
#         arbitrary_types_allowed=False,

#     )
#     field:str
#     value:str


class QueryParams(BaseModel):
    sorts: SortParamsDep
    filters: FilterParamsDep
    limit: LimitParamDep
    offset: OffsetParamDep


# async def parse_sorts(sorts:List[SortParam] = Query(default=[])) -> List[SortParam]:
#     import json
#     parsed_sorts = json.loads(sorts)
#     return [SortParam(**sort) for sort in parsed_sorts]


async def get_query_params(
    limit: LimitParamDep,
    offset: OffsetParamDep,
    filters: FilterParamsDep,
    sorts: SortParamsDep,
) -> QueryParams:
    params = QueryParams(
        filters=filters, limit=limit, sorts=sorts, offset=offset
    )
    return params


QueryParamsDep = Annotated[QueryParams, Depends(get_query_params)]
