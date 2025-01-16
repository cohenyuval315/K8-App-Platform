from typing import Annotated

from pydantic import StringConstraints

UserNameType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=None,
        min_length=4,
        pattern="^[A-Za-z][A-Za-z0-9_]*",  # {7,29} , "^[A-Za-z][A-Za-z0-9_]{7,29}$"
    ),
]
