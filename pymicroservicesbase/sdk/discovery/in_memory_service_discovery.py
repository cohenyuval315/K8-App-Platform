from typing import Any, List
from pymicroservicesbase.sdk.discovery.service_discovery_service import (
    ServiceDiscovery,
)
from pymicroservicesbase.sdk.registery.service_registery import ServiceRegistry


class InMemoryServiceDiscovery(ServiceDiscovery):
    """
    A simple in-memory service discovery mechanism.
    Queries the in-memory service registry to discover services.
    """

    def __init__(self, registry: ServiceRegistry):
        self.registry = registry

    async def discover_service(self, service_key: str) -> Any:
        """
        Discover a service by its name from the registry.
        """
        return await self.registry.get_registered_service(service_key)

    async def discover_all_services(self) -> List[Any]:
        """
        Get a list of all registered services.
        """
        return await self.registry.get_all_registered_services()
