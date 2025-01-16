import logging
from typing import Dict, List, Optional
from .json_formatter import JsonFormatter
from .string_formatter import StringFormatter
from .log_level import LogLevel
from .logging_manager import LoggingManager
from .warning_collector import WarningsCollector, WarningsCollectorHandler
from .log_level_type import LogLevelType


class LoggerFactory:
    def create_logger(
        self,
        name: Optional[str] = None,
        level: LogLevelType = LogLevel.DEBUG,
        string_formatter: StringFormatter | None = None,
        json_formatter: JsonFormatter | None = None,
        loggers_levels: Optional[Dict[str, dict]] = None,
        remove_loggers: Optional[List[str]] = None,
        **kwargs,
    ):
        """
        Create a custom logger with specified parameters.
        :param name: Name of the logger.
        :param level: Logging level (e.g., logging.DEBUG, logging.INFO).
        :param log_to_file: Whether to log to a file (default is False).
        :param file_name: The name of the log file (used if log_to_file is True).
        :param format_str: The format string for log messages.
        :return: Configured logger instance.
        """
        if string_formatter is None:
            string_formatter = StringFormatter(**kwargs)
        logger = logging.getLogger(name)
        logger.setLevel(level)

        WarningsCollector.logger = logger
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(string_formatter)
        logger.addHandler(stream_handler)

        if json_formatter:
            json_stream_handler = logging.StreamHandler()
            json_stream_handler.setFormatter(json_formatter)
            logger.addHandler(json_stream_handler)

        logger.addHandler(WarningsCollectorHandler(level=LogLevel.WARNING))
        LoggingManager.add_logger(logger.name, int(level), stream_handler)

        if remove_loggers is not None:
            for remove_logger in remove_loggers:
                LoggingManager.remove_logger(remove_logger)

        if loggers_levels:
            for _name, config in loggers_levels.items():
                LoggingManager.change_logger_level(_name, int(config["level"]))

        return logger
