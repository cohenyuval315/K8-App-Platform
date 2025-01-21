from typing import Optional
import logging


class WarningsCollector:
    """Warnings Collector"""

    logger: Optional[logging.Logger] = None
    warnings = {}

    @classmethod
    def flush(cls):
        """
        flush all warnings
        """
        if cls.logger:
            for text, count in cls.warnings.items():
                cls.logger.info(
                    f"""
                    \n----------WARNING-------------\n
                        warning count: {count}\n
                        warning text: {text}\n
                    \n----------END WARNING---------\n
                """
                )
            cls.warnings = {}

    @classmethod
    def warn(cls, text):
        """_summary_

        Args:
            text (_type_): _description_
        """
        if text not in cls.warnings:
            cls.warnings[text] = 0
        cls.warnings[text] += 1


class WarningsCollectorHandler(logging.Handler):
    """Custom handler to collect warning logs automatically"""

    def __init__(self, level=logging.WARNING):
        super().__init__(level)

    def emit(self, record: logging.LogRecord):
        if record.levelname.upper() == "WARNING":
            message = self.format(record)
            WarningsCollector.warn(message)
