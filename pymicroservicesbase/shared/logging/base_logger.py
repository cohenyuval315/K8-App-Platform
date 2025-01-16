import logging
from .abstract_logger import AbstractLogger


class BaseLogger(AbstractLogger):
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)

    def trace(self, level, msg, stack_level=1, *args, **kwargs):
        self.logger.log(
            level,
            msg,
            stack_level * args,
            **kwargs,
            exc_info=True,
            stack_info=True,
        )

    def exception(self, exception, *args, **kwargs):
        self.logger.exception(exception, *args, **kwargs, exc_info=True)
