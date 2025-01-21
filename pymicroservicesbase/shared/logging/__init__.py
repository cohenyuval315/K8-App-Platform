from .logger_factory import get_logger
import logging as lg


ROOT = "pymicroservicesbase"

DEBUG = lg.DEBUG
INFO = lg.INFO
WARN = lg.WARN
WARNING = lg.WARNING
CRITICAL = lg.CRITICAL
ERROR = lg.ERROR
FATAL = lg.FATAL
NOTSET = lg.NOTSET

TRACE = 5
lg.addLevelName(TRACE, "TRACE")

levels = {
    "debug": DEBUG,
    "info": INFO,
    "warn": WARN,
    "warning": WARNING,
    "critical": CRITICAL,
    "error": ERROR,
    "fatal": FATAL,
    "notset": NOTSET,
    "trace": TRACE,
}

levels_nums = list(levels.values())


def normalize_log_level(log_level: int | str):
    try:
        if isinstance(log_level, int):
            if log_level not in levels_nums:
                raise ValueError(f"invalid log level {log_level}")
            return log_level
        elif isinstance(log_level, str):
            return levels.get(log_level.lower())
    except KeyError:
        raise ValueError(f"invalid log level {log_level}")


lg.basicConfig(filename="logging.conf", filemode="w")

logger = get_logger(name=ROOT, level=lg.DEBUG, propagate=True)
