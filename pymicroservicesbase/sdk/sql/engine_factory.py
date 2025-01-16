from typing import Any
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


class EngineFactory:
    def create_engine(
        self, url: str | URL, *args: Any, **kwargs: Any
    ) -> AsyncEngine:
        return create_async_engine(url, *args, **kwargs)
