from enum import Enum
from typing import Union, Literal


class LogLevel(int, Enum):
    """
    Enum representing log levels.
    Literal types for clarity:
        - CRITICAL: "CRITICAL", "critical", 50
        - ERROR: "ERROR", "error", 40
        - WARNING: "WARNING", "warning", 30
        - INFO: "INFO", "info", 20
        - DEBUG: "DEBUG", "debug", 10
        - TRACE: "TRACE", "trace", 5
        - NOTSET: "NOTSET", "notset", 0
    """

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    TRACE = 5
    NOTSET = 0

    # def __new__(cls, value):
    #     obj = int.__new__(cls, value)
    #     obj._value_ = value
    #     return obj

    def __int__(self) -> int:
        return self._value_

    def __str__(self) -> str:
        return self.name.lower()

    @classmethod
    def parse(
        cls,
        level: Union[
            str,
            int,
            Literal[
                "critical",
                "CRITICAL",
                50,
                "error",
                "ERROR",
                40,
                "warning",
                "WARNING",
                30,
                "info",
                "INFO",
                20,
                "debug",
                "DEBUG",
                10,
                "trace",
                "TRACE",
                5,
                "notset",
                "NOTSET",
                0,
            ],
        ],
    ):
        """
        Parse the input level (string, int, or literal) and return the corresponding LogLevel.
        """
        if isinstance(level, int):
            for log_level in cls:
                if log_level == level:
                    return log_level
            raise ValueError(f"Invalid log level integer: {level}")

        if isinstance(level, str):
            normalized = level.upper()
            for log_level in cls:
                if log_level.name == normalized:
                    return log_level
            raise ValueError(f"Invalid log level string: {level}")

        raise TypeError(f"Invalid log level type: {type(level).__name__}")
