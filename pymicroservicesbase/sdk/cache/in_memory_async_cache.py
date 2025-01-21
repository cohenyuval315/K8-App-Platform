import asyncio
from typing import Any, Dict, List, Optional
from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)
from datetime import datetime
from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_timestamp,
)
from pymicroservicesbase.utils.datetime_utils.date_time import datetime_to_utc


class TestLock:
    def __init__(self):
        self.lock = asyncio.locks.Lock()

    async def __aenter__(self, *exc_info):
        pass

    async def __aexit__(self, *exc_info):
        pass


class InMemoryAsyncCache(AbstractAsyncCache):
    def __init__(self):
        self._store = {}
        self._lock = TestLock()
        self._ttl_store: Dict[str, datetime] = {}

    # @contextlib.asynccontextmanager
    # async def _lock(self):
    #     return TestLock()

    async def get_all(self, *args: Any, **kwargs: Any) -> Any:
        return (self._store, self._ttl_store)

    async def connect(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        pass

    async def close(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        pass

    async def _cleanup_expired_key(self, key: str):
        entry = self._store.get(key)
        if entry is not None:
            expire_at = self._ttl_store.get(key, None)
            if expire_at is not None:
                remaining = await self._get_remaining_ttl(expire_at)
                if remaining <= 0:
                    del self._store[key]
                    del self._ttl_store[key]
                    return key
        return None

    async def _cleanup_expired(self) -> List[str]:
        async with self._lock:
            results = []
            for key, value in self._store.items():
                result = await self._cleanup_expired_key(key)
                if result is not None:
                    results.append(result)
            return results

    # Key Operations
    async def get_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        async with self._lock:
            await self._cleanup_expired()
            entry = self._store.get(key, None)
            if entry is not None:
                return entry

    async def set_key(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            self._store[key] = value
            self._ttl_store.pop(key, None)
            return True

    async def delete_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        async with self._lock:
            self._store.pop(key, None)
            self._ttl_store.pop(key, None)
            return key

    async def delete_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            results = []
            for key in keys:
                results.append(await self.delete_key(key))
            return results

    async def get_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any]:
        async with self._lock:
            await self._cleanup_expired()
            results = []
            for key in keys:
                value = self._store.get(key, None)
                results.append(value)
            return results

    async def key_exists(self, key: str, *args: Any, **kwargs: Any) -> bool:
        async with self._lock:
            await self._cleanup_expired_key(key)
            return key in self._store

    async def get_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Optional[datetime]:
        async with self._lock:
            await self._cleanup_expired_key(key)
            dt = self._ttl_store.get(key, None)
            return dt

    async def set_expire_datetime(
        self, key: str, dt: datetime, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is None:
                return False

            dt_utc = datetime_to_utc(dt)
            current_utc = await self._current_datetime()
            delta = dt_utc - current_utc
            if delta.total_seconds() <= 0:
                return False

            self._ttl_store[key] = dt_utc
            return True

    async def remove_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is None:
                return False
            expired_at = self._ttl_store.pop(key, None)
            return expired_at

    async def get_ttl(self, key: str) -> int | None:
        """Get the remaining TTL for a key."""
        async with self._lock:
            expire_at = await self.get_expire_datetime(key)
            if expire_at is None:
                return None

            remaining = await self._get_remaining_ttl(expire_at)
            return max(0, int(remaining))

    async def remove_ttl(self, key: str):
        """Remove TTL from a key."""
        async with self._lock:
            expired_at = self._ttl_store.pop(key, None)
            if expired_at is not None:
                remaining = await self._get_remaining_ttl(expired_at)
                return remaining

    async def set_ttl(self, key: str, ttl: int):
        """Set a TTL for a key."""
        async with self._lock:
            if key in self._store:
                expire_at = await self._current_datetime_with_ttl(ttl)
                self._ttl_store[key] = expire_at
                return True

    async def set_expire_timestamp(
        self, key: str, timestamp: float, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            expire_dt = await self._timestmap_to_datetime(timestamp)
            return await self.set_expire_datetime(key, expire_dt)

    async def get_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Optional[float]:
        async with self._lock:
            expired_at = await self.get_expire_datetime(key)
            if expired_at is not None:
                return datetime_to_timestamp(expired_at)
            return None

    async def remove_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            expired_at = await self.remove_expire_datetime(key)
            if expired_at is not None:
                return datetime_to_timestamp(expired_at)

    async def increment_key(
        self, key: str, value: int, *args: Any, **kwargs: Any
    ) -> int | None:
        async with self._lock:
            _value = self._store.get(key, None)
            if _value is not None and _value.isdigit():
                new_value = _value + value
                self._store[key] = new_value
                return new_value

    async def decrement_key(
        self, key: str, value: int, *args: Any, **kwargs: Any
    ) -> int | None:
        async with self._lock:
            return await self.increment_key(key, -1 * value, *args, **kwargs)

    async def create_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        async with self._lock:
            self._store[key] = set()
            return True

    async def add_to_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                entry.add(value)
                return value
            self._store[key] = set(value)

    async def remove_from_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                try:
                    entry.remove(value)
                    return value
                except KeyError:
                    return None

    async def delete_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        return await self.delete_key(key)

    async def get_set_size(self, key: str, *args: Any, **kwargs: Any) -> int:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                return len(entry)
            return -1

    async def set_contains(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                return value in entry

            return False

    async def set_exists(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool:
        return await self.set_contains(key, value)

    async def get_set_members(
        self, key: str, *args: Any, **kwargs: Any
    ) -> List[Any]:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                return list(entry)
            return []

    async def get_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Optional[Any]:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, set):
                # size = await self.get_set_size(key)
                # random.randint(0, size)
                pass

    async def pop_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Optional[Any]:
        async with self._lock:
            pass

    async def get_multiple_randoms_members_from_set(
        self, key: str, count: int, *args: Any, **kwargs: Any
    ) -> List[Any]:
        async with self._lock:
            return []

    async def set_flat_mapping(
        self, key: str, mapping: dict, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            self._store[key] = mapping
            self._ttl_store.pop(key, None)
            return True

    async def flat_mapping_contains_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Optional[Any]:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, dict):
                return entry.get(field, None) is not None

    async def get_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Optional[Any]:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, dict):
                return entry.get(field, None)

    async def set_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None:
                if isinstance(entry, dict):
                    entry[field] = value
                    return value
            self._store[key] = {field: value}

    async def delete_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, dict):
                return entry.pop(field, None)

    async def update_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        return await self.set_flat_mapping_key(key, field, value)

    async def get_all_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Optional[dict]:
        async with self._lock:
            entry = self._store.get(key, None)
            if entry is not None and isinstance(entry, dict) and entry:
                return entry

    async def delete_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        return await self.delete_key(key)
