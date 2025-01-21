from typing import Any
from pydantic import Field
from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pymicroservicesbase.utils.tokens.base_token_factory import (
    BaseTokenFactory,
)
import pyotp
from datetime import datetime


class TOTPConfig(BaseModel):
    secret_key: str | None = Field(title="secret key", alias="s")

    digits: int | None = Field(title="digits", alias="digits")

    digest: Any | None = Field(title="digest", alias="digest")

    name: str | None = Field(title="name", alias="name")

    issuer: str | None = Field(title="issuer", alias="issuer")

    interval: int | None = Field(title="interval", alias="interval")

    valid_window: int | None = Field(
        title="valid_window", alias="valid_window"
    )

    offset_counter: int | None = Field(
        title="offset_counter", alias="offset_counter"
    )

    for_time: datetime | None = Field(title="for_time", alias="for_time")


class TOTPTokenFactory(BaseTokenFactory):
    token_type = "totp"

    def _get_totp(self) -> pyotp.TOTP:
        totp = pyotp.TOTP(
            s=getattr(self, "s"),
            digits=getattr(self, "digits"),
            digest=getattr(self, "digest"),
            name=getattr(self, "name", None),
            issuer=getattr(self, "issuer", None),
            interval=getattr(self, "interval"),
        )
        return totp

    def _verify_token(
        self,
        token: str,
        for_time: datetime | None = None,
        valid_window: int = 0,
    ) -> bool:
        totp = self._get_totp()
        is_verified = totp.verify(
            otp=token, for_time=for_time, valid_window=valid_window
        )
        return is_verified

    def _generate_token(
        self, for_time: int | datetime | None, counter_offset: int = 0
    ) -> str:
        totp = self._get_totp()
        if for_time is None:
            return totp.now()
        else:
            return totp.at(for_time=for_time, counter_offset=counter_offset)

    def _configure(self, totp_config: TOTPConfig | None = None):
        if totp_config is not None:
            config = totp_config.model_dump(
                exclude_unset=True, exclude_none=False, by_alias=True
            )
            for k, v in config.items():
                setattr(self, k, v)
