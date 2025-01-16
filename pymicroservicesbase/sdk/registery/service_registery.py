from abc import ABC, abstractmethod
from typing import Any, Tuple


class ServiceRegistry(ABC):
    """
    Abstract class for a service registry where services can register themselves.
    """

    @abstractmethod
    async def register_service(
        self,
        service_key: str,
        service_registration_data: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Register a service in the registry.
        """
        raise NotImplementedError

    @abstractmethod
    async def deregister_service(
        self, service_key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """
        Deregister a service from the registry.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_registered_service(
        self, service_key: str, *args: Any, **kwargs: Any
    ) -> Tuple[str, int]:
        """ """
        raise NotImplementedError

    @abstractmethod
    async def get_all_registered_services(self):
        """
        Get all registered services.
        """
        raise NotImplementedError
