from typing import Annotated

from pydantic import StringConstraints

PassWordStrType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=None,
        min_length=4,
        pattern=None,
    ),
]
