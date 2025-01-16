import logging

from pymicroservicesbase.shared.logging.base_logger import BaseLogger

from .create_logger import create_logger


class RootLogger(BaseLogger):
    def __init__(self):
        logger = create_logger(
            name="pymicroservicesbase",
            level=logging.DEBUG,
            remove_loggers=["faker", "faker.factory"],
        )
        super().__init__(logger)


logger = RootLogger()

faker_logger = logging.getLogger("faker")
faker_logger.setLevel(logging.CRITICAL)

# epol_logger = logging.getLogger("pytest")
# epol_logger.setLevel(logging.CRITICAL)
