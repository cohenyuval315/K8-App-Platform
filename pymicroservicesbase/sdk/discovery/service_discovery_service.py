class ServiceDiscoveryService:
    def __init__(self):
        self.services = {
            "auth": "http://authentication:8001",
            "users": "http://users:8002",
            "_auth": {
                "url": "http://authentication:8001",
            },
        }

    def get_service_url(self, path: str):
        service_prefix = path.split("/")[0]
        return self.services[service_prefix]
