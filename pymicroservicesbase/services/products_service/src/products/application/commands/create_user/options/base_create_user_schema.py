from pydantic import ConfigDict
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class BaseCreateUserSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")
