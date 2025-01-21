import redis.asyncio as redis
from typing import Any, Awaitable, List
from datetime import datetime, timedelta
from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow


class RedisAsyncCache(AbstractAsyncCache):
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self._client = redis.Redis(
            host=host, port=port, db=db, decode_responses=True
        )

    @property
    def client(self) -> redis.Redis:
        """
        Getter for client
        """
        try:
            return self._client
        except Exception as e:
            raise e
        finally:
            pass

    @client.setter
    def client(self, value: redis.Redis):
        """
        Setter for client
        """
        self._client = value

    async def connect(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        return await self.client.ping()

    async def close(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        return await self.client.aclose()

    # Key Operations
    async def get_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        return await self._client.get(key)

    async def set_key(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.set(key, value)

    async def delete_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        return await self._client.delete(key)

    async def delete_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.delete(*keys)

    async def get_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any | None:
        return await self._client.mget(keys)

    async def key_exists(
        self, key: str, *args: Any, **kwargs: Any
    ) -> bool | Any:
        return await self._client.exists(key) == 1

    async def get_ttl(self, key: str, *args: Any, **kwargs: Any) -> int | Any:
        ttl = await self._client.ttl(key)
        if ttl == -1:
            return None
        return ttl

    async def set_ttl(
        self, key: str, ttl: int, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.expire(key, ttl)

    async def remove_ttl(self, key: str, *args: Any, **kwargs: Any) -> Any:
        return await self._client.persist(key)

    async def set_expire_timestamp(
        self, key: str, timestamp: float, *args: Any, **kwargs: Any
    ) -> Any:
        # return await self._client.expireat(key, timestamp)
        raise NotImplementedError

    async def get_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> float | Any:
        raise NotImplementedError
        # ttl = await self._client.ttl(key)
        # return utcnow().timestamp() + ttl if ttl > 0 else None

    async def remove_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        raise NotImplementedError
        # return await self._client.persist(key)

    async def set_expire_datetime(
        self, key: str, dt: datetime, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.expireat(key, int(dt.timestamp()))

    async def get_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> datetime | Any:
        ttl = await self._client.ttl(key)
        if ttl > 0:
            return utcnow() + timedelta(seconds=ttl)
        return None

    async def remove_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.persist(key)

    # Integers Operations
    async def increment_key(
        self, key: str, value: int, *args: Any, **kwargs: Any
    ) -> int | Any:
        return await self._client.incrby(key, value)

    async def decrement_key(
        self, key: str, value: int, *args: Any, **kwargs: Any
    ) -> int | Any:
        return await self._client.decrby(key, value)

    # String Operations
    async def set_string(
        self, key: str, value: str, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.set(key, value)

    async def get_string(
        self, key: str, *args: Any, **kwargs: Any
    ) -> str | None | Any:
        return await self._client.get(key)

    async def get_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        return await self._client.mget(keys)

    async def delete_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        return await self._client.delete(*keys)

    # Set Operations
    async def create_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> int | Any:
        result = self._client.sadd(key, *["default"])
        if isinstance(result, Awaitable):
            result = await result
        await self.remove_from_set(key, "default")
        return result

    async def add_to_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> int | Any:
        result = self._client.sadd(key, value)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def remove_from_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        result = self._client.srem(key, value)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def delete_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        return await self._client.delete(key)

    async def get_set_size(
        self, key: str, *args: Any, **kwargs: Any
    ) -> int | Any:
        result = self._client.scard(key)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def set_contains(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        result = self._client.sismember(key, value)
        if isinstance(result, Awaitable):
            result = await result
        return bool(result)

    async def set_exists(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        result = self.set_contains(key, value)
        if isinstance(result, Awaitable):
            result = await result
        return bool(result)

    async def get_set_members(
        self, key: str, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        result = self._client.smembers(key)
        if isinstance(result, Awaitable):
            result = await result
        return list(result)

    async def get_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        result = self._client.srandmember(key)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def pop_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        result = self._client.spop(key)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def get_multiple_randoms_members_from_set(
        self, key: str, count: int, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        result = self._client.srandmember(key, count)
        if isinstance(result, Awaitable):
            result = await result
        return result

    # Mapping Operations
    async def set_flat_mapping(
        self, key: str, mapping: dict, *args: Any, **kwargs: Any
    ) -> Any | None:
        result = self._client.hset(key, None, None, mapping)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def get_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        result = self._client.hget(key, field)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def set_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        result = self._client.hset(key, field, value)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def delete_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any:
        result = self._client.hdel(key, field)
        if isinstance(result, Awaitable):
            result = await result
        return result

    async def update_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        return await self.set_flat_mapping_key(key, field, value)

    async def get_all_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> dict | Any:
        result = self._client.hgetall(key)
        if isinstance(result, Awaitable):
            result = await result
        if not result:
            return None
        return result

    async def delete_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        return await self._client.delete(key)
