from pydantic import ConfigDict

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel


class BaseWebCommand(BaseModel):
    """
    Base model for web commands with stricter validation rules.
    """

    model_config: ConfigDict = ConfigDict(
        arbitrary_types_allowed=True,
        extra="ignore",
        from_attributes=True,
        populate_by_name=True,
    )
