from abc import ABC, abstractmethod
from typing import Any


class ServiceDiscovery(ABC):
    """
    Abstract class for a service discovery mechanism.
    Services can query the registry to discover other services.
    """

    @abstractmethod
    async def discover_service(
        self, service_key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """
        Discover a registered service by its name.
        Returns the host and port of the service.
        """
        raise NotImplementedError

    @abstractmethod
    async def discover_all_services(self, *args: Any, **kwargs: Any) -> Any:
        """
        Discover all available services.
        """
        raise NotImplementedError
