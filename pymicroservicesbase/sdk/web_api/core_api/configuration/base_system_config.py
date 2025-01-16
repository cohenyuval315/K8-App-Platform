from typing import Any
from pydantic_settings import BaseSettings


class BaseSystemConfig(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    DEBUG: bool = False
    ENVIRONMENT: str
    DEBUGGER_PORT: int = 5678
    DEBUGGER_HOST: str = "0.0.0.0"

    ROOT_PATH: str = "/"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"

    ALLOW_ORIGINS: Any
    ALLOW_CREDS: Any
    ALLOW_METHODS: Any
    ALLOW_HEADERS: Any
    ALLOWED_HOSTS: Any

    PRINT_APP: bool
    PRINT_ENVIRONMENT: bool
