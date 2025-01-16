from pydantic import ConfigDict, Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class ProductPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")
    product_id: str = Field(...)
