from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class SessionPayload(BaseModel):
    session_id: str
    extend_count: int = 0
