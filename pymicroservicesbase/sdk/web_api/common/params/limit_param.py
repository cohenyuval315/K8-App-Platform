from fastapi import Depends, Query

from typing import Annotated

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class LimitParam(BaseModel):
    limit: int


async def get_limit(
    limit: int = Query(default=1, gt=0, alias="page_size"),
) -> int:
    return limit


LimitParamDep = Annotated[int, Depends(get_limit)]
