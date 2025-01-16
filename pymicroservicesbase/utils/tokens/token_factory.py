from typing import Dict, Self

from pymicroservicesbase.utils.tokens.jwt_token_factory import JWTTokenFactory

from .base_token_factory import BaseTokenFactory
from .token_type import TokenType
from .totp_token_factory import TOTPTokenFactory
from .uuid_token_factory import UUIDTokenFactory


class TokenFactory:
    def __init__(self):
        self.factories: Dict[TokenType, BaseTokenFactory] = {
            TokenType.JWT: JWTTokenFactory(),
            TokenType.UUID: UUIDTokenFactory(),
            TokenType.TOTP: TOTPTokenFactory(),
        }

    def configure(self, token_type: TokenType, *args, **kwargs) -> Self:
        self.get(token_type, *args, **kwargs)
        return self

    def get(self, token_type: TokenType, *args, **kwargs) -> BaseTokenFactory:
        try:
            factory = self.factories[token_type]
            return factory.configure(*args, **kwargs)
        except KeyError:
            raise ValueError(
                f"factory does not exists for token type {token_type}"
            )
