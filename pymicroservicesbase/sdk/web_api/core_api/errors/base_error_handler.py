from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from fastapi import Request, Response


T = TypeVar("T", bound=Exception)


class BaseErrorHandler(Generic[T], ABC):
    """Base class for error handlers."""

    def __init__(self, exception_cls: type[T] | None = None, **kwargs) -> None:
        if not hasattr(self, "exception_cls"):
            if exception_cls is not None:
                self.exception_cls = exception_cls
            else:
                raise TypeError(
                    "Cannot instantiate BaseErrorHandler without specifying the generic type."
                )

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if hasattr(cls, "__orig_bases__"):
            for base in cls.__orig_bases__:  # type: ignore
                if hasattr(base, "__args__"):
                    cls.exception_cls = base.__args__[0]  # Extract T

    @abstractmethod
    async def exception_handler(
        self, request: Request, exc: T
    ) -> Response | Any:
        """exception_handler method."""
        raise NotImplementedError
