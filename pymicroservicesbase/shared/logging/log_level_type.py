from typing import Literal
from .log_level import LogLevel

LogLevelType = (
    LogLevel
    | str
    | int
    | Literal[
        "trace",
        "TRACE",
        5,
        "debug",
        "DEBUG",
        10,
        "info",
        "INFO",
        20,
        "error",
        "ERROR",
        30,
        "warning",
        "WARNING",
        40,
        "critical",
        "CRITICAL",
        50,
    ]
)
