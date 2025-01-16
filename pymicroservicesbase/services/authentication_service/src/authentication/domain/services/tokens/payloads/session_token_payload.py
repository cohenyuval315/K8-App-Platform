from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from .session_payload import SessionPayload
from .user_payload import UserPayload
from .product_payload import ProductPayload


class SessionTokenPayload(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    session: SessionPayload
    user: UserPayload
    product: ProductPayload
