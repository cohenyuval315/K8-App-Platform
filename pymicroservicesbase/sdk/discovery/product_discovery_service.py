from typing import Any, Dict


class LoginConfig:
    pass


class PymicroservicesbaseProduct:
    product_key: str
    product_id: str
    title: str
    config: Dict[str, Any] | Any


class ProductDiscoveryService:
    def __init__(self):
        self.products = {
            "demo": {
                "id": "demo_project_id",
                "title": "demo",
                "config": {"login": {}},
            },
        }
        self.product_keys = {"something_wierd_demo_key": "demo"}

    def get_product_config_by_key(self, product_key: str):
        return self.products[self.product_keys[product_key]]

    def get_product_config(self, product_id: str):
        return self.products[product_id]
