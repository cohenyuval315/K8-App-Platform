from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from .access_payload import AccessPayload
from .user_payload import UserPayload
from .product_payload import ProductPayload


class AccessTokenPayload(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    access: AccessPayload
    user: UserPayload
    product: ProductPayload
