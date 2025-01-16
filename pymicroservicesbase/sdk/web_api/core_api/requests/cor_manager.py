from typing import Callable
from uuid import uuid4
from pymicroservicesbase.sdk.web_api.core_api.requests.correlation_id_handler import (
    CorrelationIdHandler,
)


def uuid_hex_generator() -> str:
    return uuid4().hex


class CorrelationIdManager:
    def __init__(self, id_generator: Callable[[], str] = uuid_hex_generator):
        self.id_generator = id_generator
        self._handlers = []

    def add_handler(self, extension: CorrelationIdHandler) -> None:
        """Register an extension to handle the correlation ID."""
        self._handlers.append(extension)

    def run_correlation_id(self, correlation_id: str) -> None:
        """Set the correlation ID and notify all extensions."""
        for handler in self._handlers:
            handler.handle_correlation_id(correlation_id)

    def generate_correlation_id(
        self, generator: Callable[[], str] = uuid_hex_generator
    ) -> str:
        """Generate a new correlation ID using the provided generator."""
        return generator()
