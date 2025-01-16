from pydantic_settings import BaseSettings
import os


class BaseRuntimeConfig(BaseSettings):
    SERVICE_HOST: str = os.environ.get("SERVICE_HOST", "0.0.0.0")
    SERVICE_PORT: int = os.environ.get("SERVICE_PORT", 8000)
    DEBUG: bool = False
    ENVIRONMENT: str
    DEBUGGER_PORT: int = 5678
    DEBUGGER_HOST: str = "0.0.0.0"
