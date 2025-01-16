from enum import Enum


class TokenType(Enum):
    UUID = "UUID"
    Random = "Random"
    JWT = "JWT"
    HMAC = "HMAC"
    Base64 = "Base64"
    TOTP = "TOTP"
    Incremental = "Incremental"
    Opaque = "Opaque"
    Timestamp = "Timestamp"
    Custom = "Custom"
