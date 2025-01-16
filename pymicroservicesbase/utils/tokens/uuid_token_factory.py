from pymicroservicesbase.utils.tokens.base_token_factory import (
    BaseTokenFactory,
)
from pymicroservicesbase.utils.id.generate_id import generate_id


class UUIDTokenFactory(BaseTokenFactory):
    def _verify_token(
        self,
        token: str,
    ) -> bool:
        raise NotImplementedError(
            "uuid token factory should not impl verify token"
        )

    def _generate_token(
        self,
    ) -> str:
        return generate_id(getattr(self, "length"))

    def _configure(self, length: int | None = None):
        if length is not None:
            self.length = length
