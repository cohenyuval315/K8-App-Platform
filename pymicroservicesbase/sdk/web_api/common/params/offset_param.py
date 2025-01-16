from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from fastapi import Depends, Query
from typing import Annotated


class OffsetParam(BaseModel):
    offset: int


async def get_offset(
    offset: int = Query(default=0, ge=0, alias="page"),
) -> int:
    return offset


OffsetParamDep = Annotated[int, Depends(get_offset)]
