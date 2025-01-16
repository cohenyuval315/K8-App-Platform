import logging
from typing import Any, Callable

from pymicroservicesbase.shared.logging.base_logger import BaseLogger

from .uvicorn_logger_type import UvicornLoggerType


class WebServiceLogger(BaseLogger):
    def __init__(
        self,
        logger: logging.Logger,
    ):
        self.logger = logger
        self.uvicorn_logger = logging.getLogger("uvicorn.asgi")
        self.callback = None
        # self.uvicorn_logger.trace = self.trace

        self.uvicorn_logger = logging.getLogger("uvicorn")
        self.uvicorn_access_logger = logging.getLogger("uvicorn.access")
        self.uvicorn_error_logger = logging.getLogger("uvicorn.error")
        self.uvicorn_asgi_logger = logging.getLogger("uvicorn.asgi")

        self.loggers: dict[UvicornLoggerType, logging.Logger] = {
            "uvicorn": self.uvicorn_logger,
            "uvicorn.access": self.uvicorn_access_logger,
            "uvicorn.error": self.uvicorn_error_logger,
            "uvicorn.asgi": self.uvicorn_asgi_logger,
        }
        # self.mute_all()

    # def mute_all(self):
    #     """Mute all loggers by setting their level to CRITICAL (or NOTSET)."""
    #     for logger in self.loggers.values():
    #         logger.setLevel(logging.CRITICAL)
    #         logger.propagate = False

    # def set_log_level(self, logger_type: UvicornLoggerType, level: int):
    #     """Set the logging level for a specific logger."""
    #     if logger_type in self.loggers:
    #         self.loggers[logger_type].setLevel(level)
    #     else:
    #         raise ValueError(f"Invalid logger type: {logger_type}")

    # def _log_if_enabled(self, level: int, msg: str, *args, **kwargs):
    #     """Internal helper to log a message if the logger's level allows it."""
    #     for logger_name, logger in self.loggers.items():
    #         if logger.isEnabledFor(level):
    #             logger.log(level, f"[{logger_name}] {msg}", *args, **kwargs)

    def run_callback(self, log_entry, *args, **kwargs) -> Any:
        if self.callback is not None:
            return self.callback(log_entry, *args, **kwargs)

    def set_callback(self, callback: Callable[..., Any]):
        self.callback = callback
