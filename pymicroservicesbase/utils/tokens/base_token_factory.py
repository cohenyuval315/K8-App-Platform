from typing import Self, TypeVar, Any
from abc import ABC, abstractmethod


class BaseTokenFactory(ABC):
    token_type = None

    def __init__(self, *args: Any, **kwargs: Any):
        self.token = None
        self.configure(*args, **kwargs)

    def get_token(self) -> str:
        if self._token is None:
            raise ValueError("when called get token, token cannot be None")
        return self._token

    def generate_token(self, *args: Any, **kwargs: Any) -> str:
        self._token = self._generate_token(*args, **kwargs)
        return self._token

    def verify_token(self, token: str, *args: Any, **kwargs: Any) -> Any:
        return self._verify_token(token, *args, **kwargs)

    def configure(self, *args: Any, **kwargs: Any) -> Self:
        self._configure(*args, **kwargs)
        return self

    @abstractmethod
    def _generate_token(self, *args: Any, **kwargs: Any) -> str:
        pass

    @abstractmethod
    def _configure(self, *args: Any, **kwargs: Any):
        pass

    @abstractmethod
    def _verify_token(self, token: str, *args: Any, **kwargs: Any) -> Any:
        pass


TokenFactoryType = TypeVar("TokenFactoryType", bound=BaseTokenFactory)
