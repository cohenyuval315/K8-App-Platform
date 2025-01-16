from typing import Annotated

from pydantic import StringConstraints

LettersOnlyType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=None,
        min_length=1,
        pattern="^[A-Za-z]",
    ),
]
