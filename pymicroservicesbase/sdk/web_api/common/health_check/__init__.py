from typing import Dict

from .base_health_check import BaseHealthCheck
from .health_checks.health_check_ping import HealthCheckPing

health_checks: Dict[str, BaseHealthCheck] = {"ping": HealthCheckPing(30)}
