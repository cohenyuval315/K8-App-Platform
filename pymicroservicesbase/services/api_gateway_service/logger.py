import logging

from pymicroservicesbase.shared.logging.create_logger import create_logger

logger = create_logger(
    name="pymicroservicesbase.api_gateway",
    level=logging.DEBUG,
    propagate=False,
)
