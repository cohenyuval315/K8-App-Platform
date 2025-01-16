from abc import ABC, abstractmethod
from typing import Any, List
from datetime import datetime, timedelta

from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_timestamp,
    timestamp_to_datetime,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow


class AbstractCache(ABC):
    _is_async = False

    async def _current_datetime(self) -> datetime:
        return utcnow()

    async def _current_datetime_with_ttl(self, ttl: float) -> datetime:
        dt = await self._current_datetime()
        dt_with_ttl = dt + timedelta(seconds=ttl)
        return dt_with_ttl

    async def _current_timestamp(self) -> float:
        dt = await self._current_datetime()
        return datetime_to_timestamp(dt)

    async def _current_timestamp_with_ttl(self, ttl: float) -> float:
        dt = await self._current_datetime_with_ttl(ttl=ttl)
        return datetime_to_timestamp(dt)

    async def _get_remaining_ttl(self, expire_dt: datetime) -> float:
        dt = await self._current_datetime()
        remaining = expire_dt - dt
        return remaining.total_seconds()

    async def _timestmap_to_datetime(self, timestamp: float) -> datetime:
        return timestamp_to_datetime(timestamp)

    @abstractmethod
    def connect(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        raise NotImplementedError

    @abstractmethod
    def close(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        raise NotImplementedError

    # Key Operations
    @abstractmethod
    def get_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Retrieve a value by key"""
        raise NotImplementedError

    @abstractmethod
    def set_key(self, key: str, value: Any, *args: Any, **kwargs: Any) -> Any:
        """Store a value by key"""
        raise NotImplementedError

    @abstractmethod
    def delete_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Delete a key from the cache"""
        raise NotImplementedError

    @abstractmethod
    def delete_keys(self, keys: List[str], *args: Any, **kwargs: Any) -> Any:
        """Delete multiple keys"""
        raise NotImplementedError

    @abstractmethod
    def get_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any | None:
        """Retrieve values for multiple keys"""
        raise NotImplementedError

    @abstractmethod
    def key_exists(self, key: str, *args: Any, **kwargs: Any) -> bool | Any:
        """Check if the key exists"""
        raise NotImplementedError

    @abstractmethod
    def get_ttl(self, key: str, *args: Any, **kwargs: Any) -> float | Any:
        """Get the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    def set_ttl(self, key: str, ttl: float, *args: Any, **kwargs: Any) -> Any:
        """Set the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    def remove_ttl(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Remove the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    def set_expire_timestamp(
        self, key: str, timestamp: float, *args: Any, **kwargs: Any
    ) -> Any:
        """Set the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    def get_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Get the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    def remove_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    def set_expire_datetime(
        self, key: str, dt: datetime, *args: Any, **kwargs: Any
    ) -> Any:
        """Set the expiration datetime of a key"""
        raise NotImplementedError

    @abstractmethod
    def get_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> datetime | Any:
        """Get the expiration datetime of a key"""
        raise NotImplementedError

    @abstractmethod
    def remove_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove the expiration datetime of a key"""
        raise NotImplementedError

    # Integers Operations
    @abstractmethod
    def increment_key(
        self, key: str, value: float, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Increment a key value"""
        raise NotImplementedError

    @abstractmethod
    def decrement_key(
        self, key: str, value: float, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Decrement a key value"""
        raise NotImplementedError

    # String Operations

    def set_string(
        self, key: str, value: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Set a string value"""
        raise NotImplementedError

    def get_string(
        self, key: str, *args: Any, **kwargs: Any
    ) -> str | None | Any:
        """Get a string value"""
        raise NotImplementedError

    def get_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Get multiple string values"""
        raise NotImplementedError

    def delete_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Delete multiple string values"""
        raise NotImplementedError

    # Set Operations
    @abstractmethod
    def create_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Create a new set"""
        raise NotImplementedError

    @abstractmethod
    def add_to_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Add a value to a set"""
        raise NotImplementedError

    @abstractmethod
    def remove_from_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove a value from a set"""
        raise NotImplementedError

    @abstractmethod
    def delete_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Delete a set"""
        raise NotImplementedError

    @abstractmethod
    def get_set_size(self, key: str, *args: Any, **kwargs: Any) -> int | Any:
        """Get the size of a set"""
        raise NotImplementedError

    @abstractmethod
    def set_contains(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        """Check if a value is a member of a set"""
        raise NotImplementedError

    @abstractmethod
    def set_exists(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        """Check if a value exists in a set"""
        raise NotImplementedError

    @abstractmethod
    def get_set_members(
        self, key: str, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Retrieve all members of a set"""
        raise NotImplementedError

    @abstractmethod
    def get_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Get a random member from a set"""
        raise NotImplementedError

    @abstractmethod
    def pop_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Pop a random member from a set"""
        raise NotImplementedError

    @abstractmethod
    def get_multiple_randoms_members_from_set(
        self, key: str, count: int, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Get multiple random members from a set"""
        raise NotImplementedError

    # Mapping Operations
    @abstractmethod
    def set_flat_mapping(
        self, key: str, mapping: dict, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Set a flat mapping"""
        raise NotImplementedError

    @abstractmethod
    def get_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Retrieve a value from a hash by field"""
        raise NotImplementedError

    @abstractmethod
    def set_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Set a value in a hash field"""
        raise NotImplementedError

    @abstractmethod
    def delete_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Delete a field from a hash"""
        raise NotImplementedError

    @abstractmethod
    def update_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Update a field in a hash"""
        raise NotImplementedError

    @abstractmethod
    def get_all_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> dict | Any:
        """Retrieve all fields and values from a hash"""
        raise NotImplementedError

    @abstractmethod
    def delete_flat_mapping(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Delete a field from a hash"""
        raise NotImplementedError
