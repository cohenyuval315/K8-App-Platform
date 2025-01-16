from typing import Any, Tuple
from pymicroservicesbase.sdk.registery.service_registery import ServiceRegistry


class InMemoryServiceRegistry(ServiceRegistry):
    """
    A simple in-memory service registry for registering services.
    """

    def __init__(self):
        self.services = {}

    async def register_service(
        self,
        service_key: str,
        service_registration_data: Tuple[str, int],
        *args: Any,
        **kwargs: Any,
    ):
        self.services[service_key] = service_registration_data

    async def deregister_service(
        self, service_name: str, *args: Any, **kwargs: Any
    ):
        if service_name in self.services:
            del self.services[service_name]

    async def get_registered_service(
        self, service_name: str, *args: Any, **kwargs: Any
    ) -> Tuple[str, int]:
        if service_name in self.services:
            return self.services[service_name]
        else:
            raise ValueError(
                f"Service '{service_name}' not found in registry."
            )

    async def get_all_registered_services(self, *args: Any, **kwargs: Any):
        """Get a list of all registered services."""
        return list(self.services.keys())
