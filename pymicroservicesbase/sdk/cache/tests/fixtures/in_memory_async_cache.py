from typing import AsyncGenerator
import pytest_asyncio

from pymicroservicesbase.sdk.cache.in_memory_async_cache import (
    InMemoryAsyncCache,
)


@pytest_asyncio.fixture
async def cache() -> AsyncGenerator[InMemoryAsyncCache]:
    """Fixture to provide InMemoryAsyncCache instance."""
    cache = InMemoryAsyncCache()
    await cache.connect()  # In case there's any connection setup
    yield cache
    await cache.close()  # Cleanup after test is done
