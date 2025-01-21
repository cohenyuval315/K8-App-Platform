from typing import Any, Dict


from pymicroservicesbase.services.authentication_service.src.authentication.domain.services.tokens.payloads import (
    AccessTokenPayload,
    SessionTokenPayload,
    RefreshTokenPayload,
)
from pymicroservicesbase.utils.tokens.token_factory import TokenFactory
from pymicroservicesbase.utils.tokens.token_type import TokenType


class TokenService:
    def __init__(
        self,
        token_factory: TokenFactory,
        # access_token_expire:int,
        # refresh_token_expire:int,
        # session_token_expire:int
    ):
        self.token_factory = token_factory
        # self.access_token_expire = access_token_expire
        # self.refresh_token_expire = refresh_token_expire
        # self.session_token_expire = session_token_expire

    async def generate_access_token(
        self, payload: AccessTokenPayload, expiration: int
    ) -> str:
        jwt_token_generator = self.token_factory.get(TokenType.JWT)
        payload_dict = payload.model_dump(
            exclude_defaults=False, exclude_unset=False, exclude_none=False
        )
        token = jwt_token_generator.generate_token(
            expiration_time_in_seconds=expiration, payload=payload_dict
        )
        return token
        # TokenPayload(
        #     token_title=TokenKeyType.ACCESS_TOKEN,
        #     token_value=token,
        #     token_expire=expiration,
        #     token_type=jwt_token_generator.token_type
        # )

    async def generate_refresh_token(
        self, payload: RefreshTokenPayload, expiration: int
    ) -> str:
        jwt_token_generator = self.token_factory.get(TokenType.JWT)
        payload_dict = payload.model_dump(
            exclude_defaults=False, exclude_unset=False, exclude_none=False
        )
        return jwt_token_generator.generate_token(
            expiration_time_in_seconds=expiration, payload=payload_dict
        )

    async def generate_session_token(
        self, payload: SessionTokenPayload, expiration: int
    ) -> str:
        jwt_token_generator = self.token_factory.get(TokenType.JWT)
        payload_dict = payload.model_dump(
            exclude_defaults=False, exclude_unset=False, exclude_none=False
        )
        return jwt_token_generator.generate_token(
            expiration_time_in_seconds=expiration, payload=payload_dict
        )

    async def generate_session_id_token(self) -> str:
        uuid_token_generator = self.token_factory.get(TokenType.UUID)
        return uuid_token_generator.generate_token()

    async def generate_csrf_token(self) -> str:
        uuid_token_generator = self.token_factory.get(TokenType.UUID)
        return uuid_token_generator.generate_token()

    async def verify_access_token(
        self, access_token: str
    ) -> AccessTokenPayload:
        payload = await self._verify_jwt_token(access_token)
        access_token_payload = AccessTokenPayload.model_validate(payload)
        return access_token_payload

    async def verify_refresh_token(
        self,
        refresh_token: str,
    ) -> RefreshTokenPayload:
        payload = await self._verify_jwt_token(refresh_token)
        refresh_token_payload = RefreshTokenPayload.model_validate(payload)
        return refresh_token_payload

    async def verify_session_token(
        self,
        session_token: str,
    ) -> SessionTokenPayload:
        payload = await self._verify_jwt_token(session_token)
        session_token_payload = SessionTokenPayload.model_validate(payload)
        return session_token_payload

    async def _verify_jwt_token(self, token: str) -> dict[str, Any]:
        payload = self.token_factory.get(TokenType.JWT).verify_token(
            token=token
        )
        return payload
