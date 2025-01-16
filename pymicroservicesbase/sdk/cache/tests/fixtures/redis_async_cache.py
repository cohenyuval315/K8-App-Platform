from typing import AsyncGenerator
import pytest_asyncio

from pymicroservicesbase.sdk.cache.redis_async_cache import RedisAsyncCache


@pytest_asyncio.fixture
async def cache() -> AsyncGenerator[RedisAsyncCache]:
    """Fixture to provide RedisAsyncCache instance."""
    cache = RedisAsyncCache("localhost", 6379, 0)
    await cache.connect()  # Connect to the Redis service
    yield cache
    await cache.close()  # Cleanup after test is done
