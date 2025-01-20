import sys

TYPED_DICT_VERSION = (3, 12)
if sys.version_info < TYPED_DICT_VERSION:
    from typing_extensions import TypedDict
else:
    from typing import TypedDict


class HealthCheck(TypedDict):  # type: ignore
    name: str
    timeout: int
