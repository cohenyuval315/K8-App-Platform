from typing import Annotated
from pyndanic import StringConstraints

FullNameType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=None,
        min_length=2,
        pattern="^[A-Za-z]+( [A-Za-z]+)?( [A-Za-z]+)+$",
    ),
]
