from __future__ import annotations

from ...core_api.base_model import BaseModel
from pydantic import ConfigDict, AliasGenerator, BeforeValidator
from datetime import timedelta
from typing import Annotated


def _validate_timedelta_field(td: timedelta | None) -> TimeDelta | None:
    """Validate the timedelta field and return it."""
    if td is None:
        return None
    return TimeDelta(
        days=td.days,
        seconds=td.seconds,
        microseconds=td.microseconds,
    )


class TimeDelta(BaseModel):
    """TimeDelta can be used to interact with datetime.timedelta objects."""

    object_type: str = "TimeDelta"
    days: int
    seconds: int
    microseconds: int

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=lambda field_name: {
                "object_type": "__type",
            }.get(field_name, field_name),
        )
    )


TimeDeltaWithValidation = Annotated[
    TimeDelta, BeforeValidator(_validate_timedelta_field)
]
