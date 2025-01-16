from abc import ABC, abstractmethod


class CorrelationIdHandler(ABC):
    @abstractmethod
    def handle_correlation_id(self, correlation_id: str) -> None:
        """Handle the correlation ID for the specific extension."""
        pass
