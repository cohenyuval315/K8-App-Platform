import logging
from typing import Optional
from .string_formatter import StringFormatter
from .warning_collector import WarningsCollector, WarningsCollectorHandler
from pythonjsonlogger.json import JsonFormatter


def get_logger(
    name: Optional[str] = None,
    level: int = logging.INFO,
    propagate: bool = False,
    **kwargs,
) -> logging.Logger:
    string_formatter = StringFormatter(**kwargs)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    WarningsCollector.logger = logger
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(string_formatter)
    logger.addHandler(stream_handler)

    json_formatter = JsonFormatter()
    json_stream_handler = logging.StreamHandler()
    json_stream_handler.setFormatter(json_formatter)
    logger.addHandler(json_stream_handler)
    logger.propagate = propagate

    logger.addHandler(WarningsCollectorHandler())
    return logger


# class Logger(logging.Logger):
#     def __init__(self, name, level = 0, propagate:bool=False, **kwargs: Any):
#         super().__init__(name, level)
#         string_formatter = StringFormatter(**kwargs)
#         stream_handler = logging.StreamHandler()
#         stream_handler.setFormatter(string_formatter)
#         self.addHandler(stream_handler)

#         json_formatter = JsonFormatter()
#         json_stream_handler = logging.StreamHandler()
#         json_stream_handler.setFormatter(json_formatter)
#         self.addHandler(json_stream_handler)

#         self.propagate = propagate
#         self.warning_collector = WarningsCollectorHandler()
#         self.addHandler(self.warning_collector)


#     def _finalize(self, name):
#         self.warning_collector.flush()
