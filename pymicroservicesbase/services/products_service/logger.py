import logging

from pymicroservicesbase.shared.logging import get_logger

logger = get_logger(
    name="pymicroservicesbase.user_service",
    level=logging.DEBUG,
    propagate=False,
)
