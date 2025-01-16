from __future__ import annotations

from typing import Annotated
import pytz

from pydantic import (
    AfterValidator,
    AwareDatetime,
)

UtcDateTime = Annotated[
    AwareDatetime, AfterValidator(lambda d: d.astimezone(pytz.utc))
]
