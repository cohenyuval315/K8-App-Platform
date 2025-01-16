from ...core_api.base_model import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class Range(BaseModel, Generic[T]):
    """Range with a lower and upper bound."""

    lower_bound: T | None
    upper_bound: T | None
