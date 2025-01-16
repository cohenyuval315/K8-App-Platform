import uuid
import os
import hashlib
import base64
import time
import pyotp
import hmac
from typing import Any, Literal
from pymicroservicesbase.utils.id.generate_id import generate_id


def generate_unique_id_token() -> str:
    return generate_id()


def create_uuid_token() -> str:
    return str(uuid.uuid4())


def create_hmac_token(
    secret_key: str,
    message: str,
    encoding: str = "utf-8",
    errors: Literal[
        "strict", "ignore", "replace", "xmlcharrefreplace"
    ] = "strict",
    digestmod=hashlib.sha256,
) -> str:
    return hmac.new(
        secret_key.encode(encoding=encoding, errors=errors),
        message.encode(encoding=encoding, errors=errors),
        digestmod,
    ).hexdigest()


def create_random_string_token(length: int, sep: str = ""):
    return create_random_bytes(length).hex(sep)


def create_random_bytes(length: int) -> bytes:
    return os.urandom(length)


def create_base64_token(length: int = 32, encoding: str = "utf-8") -> str:
    if length % 2 != 0:
        raise ValueError("length must be divided by 2")
    random_bytes = create_random_bytes(length)
    base = base64.b64encode(random_bytes)
    return base.decode(encoding)


def create_otp_token(
    secret_key: str,
    digits: int = 6,
    digest: Any = None,
    name: str | None = None,
    issuer: str | None = None,
    interval: int = 30,
) -> str:
    return pyotp.TOTP(
        secret_key,
        digits=digits,
        digest=digest,
        name=name,
        issuer=issuer,
        interval=interval,
    ).now()


def create_opaque_token(length: int):
    return create_random_bytes(length).hex()


def create_timestamp_token(expiration_time: int = 3600):
    return int(time.time()) + expiration_time
