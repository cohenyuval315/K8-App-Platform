from .create_logger import create_logger
from .root_logger import logger
import logging as lg


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


# loggers = {
#     "sqlalchemy",
#     "sqlalchemy.engine",
#     "sqlalchemy.pool",
#     "sqlalchemy.dialects",
#     "sqlalchemy.orm",
#     "faker"
# "uvicorn",
# "uvicorn.access",
# "uvicorn.error",
# "uvicorn.asgi",
# }


# import sentry_sdk

# sentry_sdk.init(
#     "https://<key>@sentry.io/<project>",

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for Tracing.
#     # We recommend adjusting this value in production.
#     enable_tracing=True,
#     traces_sample_rate=1.0,
# )
