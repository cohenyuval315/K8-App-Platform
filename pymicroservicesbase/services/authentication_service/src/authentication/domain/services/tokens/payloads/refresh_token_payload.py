from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from .login_payload import LoginPayload
from .user_payload import UserPayload
from .product_payload import ProductPayload


class RefreshTokenPayload(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    user: UserPayload
    product: ProductPayload
    login: LoginPayload
