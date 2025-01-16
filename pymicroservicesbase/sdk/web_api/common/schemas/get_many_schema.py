from pydantic import Field
from pymicroservicesbase.sdk.web_api.common.params.query_params import (
    QueryParams,
)


class GetManySchema(QueryParams):
    offset: int = Field()
    limit: int = Field()
    sorts: list
    filters: list
