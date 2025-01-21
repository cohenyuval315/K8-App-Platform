import logging

from pymicroservicesbase.shared.logging import get_logger

logger = get_logger(
    name="pymicroservicesbase.api_gateway",
    level=logging.DEBUG,
    propagate=False,
)
