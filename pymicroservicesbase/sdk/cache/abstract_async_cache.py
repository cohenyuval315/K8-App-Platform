from abc import ABC, abstractmethod
from typing import Any, List
from pymicroservicesbase.sdk.cache.abstract_cache import AbstractCache
from datetime import datetime


class AbstractAsyncCache(AbstractCache, ABC):
    _is_async = True

    async def get_all(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def connect(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        raise NotImplementedError

    @abstractmethod
    async def close(self, *args: Any, **kwargs: Any) -> Any:
        """cleanup"""
        raise NotImplementedError

    # Key Operations
    @abstractmethod
    async def get_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Retrieve a value by key"""
        raise NotImplementedError

    @abstractmethod
    async def set_key(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Store a value by key"""
        raise NotImplementedError

    @abstractmethod
    async def delete_key(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Delete a key from the cache"""
        raise NotImplementedError

    @abstractmethod
    async def delete_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> Any:
        """Delete multiple keys"""
        raise NotImplementedError

    @abstractmethod
    async def get_keys(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any | None:
        """Retrieve values for multiple keys"""
        raise NotImplementedError

    @abstractmethod
    async def key_exists(
        self, key: str, *args: Any, **kwargs: Any
    ) -> bool | Any:
        """Check if the key exists"""
        raise NotImplementedError

    @abstractmethod
    async def get_ttl(
        self, key: str, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Get the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    async def set_ttl(
        self, key: str, ttl: float, *args: Any, **kwargs: Any
    ) -> Any:
        """Set the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    async def remove_ttl(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Remove the TTL of a key"""
        raise NotImplementedError

    @abstractmethod
    async def set_expire_timestamp(
        self, key: str, timestamp: float, *args: Any, **kwargs: Any
    ) -> Any:
        """Set the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    async def get_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Get the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    async def remove_expire_timestamp(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove the expiration timestamp of a key"""
        raise NotImplementedError

    @abstractmethod
    async def set_expire_datetime(
        self, key: str, dt: datetime, *args: Any, **kwargs: Any
    ) -> Any:
        """Set the expiration datetime of a key"""
        raise NotImplementedError

    @abstractmethod
    async def get_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> datetime | Any:
        """Get the expiration datetime of a key"""
        raise NotImplementedError

    @abstractmethod
    async def remove_expire_datetime(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove the expiration datetime of a key"""
        raise NotImplementedError

    # Integers Operations
    @abstractmethod
    async def increment_key(
        self, key: str, value: float, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Increment a key value"""
        raise NotImplementedError

    @abstractmethod
    async def decrement_key(
        self, key: str, value: float, *args: Any, **kwargs: Any
    ) -> float | Any:
        """Decrement a key value"""
        raise NotImplementedError

    # String Operations

    async def set_string(
        self, key: str, value: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Set a string value"""
        raise NotImplementedError

    async def get_string(
        self, key: str, *args: Any, **kwargs: Any
    ) -> str | None | Any:
        """Get a string value"""
        raise NotImplementedError

    async def get_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Get multiple string values"""
        raise NotImplementedError

    async def delete_strings(
        self, keys: List[str], *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Delete multiple string values"""
        raise NotImplementedError

    # Set Operations
    @abstractmethod
    async def create_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Create a new set"""
        raise NotImplementedError

    @abstractmethod
    async def add_to_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Add a value to a set"""
        raise NotImplementedError

    @abstractmethod
    async def remove_from_set(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Remove a value from a set"""
        raise NotImplementedError

    @abstractmethod
    async def delete_set(self, key: str, *args: Any, **kwargs: Any) -> Any:
        """Delete a set"""
        raise NotImplementedError

    @abstractmethod
    async def get_set_size(
        self, key: str, *args: Any, **kwargs: Any
    ) -> int | Any:
        """Get the size of a set"""
        raise NotImplementedError

    @abstractmethod
    async def set_contains(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        """Check if a value is a member of a set"""
        raise NotImplementedError

    @abstractmethod
    async def set_exists(
        self, key: str, value: Any, *args: Any, **kwargs: Any
    ) -> bool | Any:
        """Check if a value exists in a set"""
        raise NotImplementedError

    @abstractmethod
    async def get_set_members(
        self, key: str, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Retrieve all members of a set"""
        raise NotImplementedError

    @abstractmethod
    async def get_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Get a random member from a set"""
        raise NotImplementedError

    @abstractmethod
    async def pop_random_member_from_set(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Pop a random member from a set"""
        raise NotImplementedError

    @abstractmethod
    async def get_multiple_randoms_members_from_set(
        self, key: str, count: int, *args: Any, **kwargs: Any
    ) -> List[Any] | Any:
        """Get multiple random members from a set"""
        raise NotImplementedError

    # Mapping Operations
    @abstractmethod
    async def set_flat_mapping(
        self, key: str, mapping: dict, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Set a flat mapping"""
        raise NotImplementedError

    @abstractmethod
    async def get_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any | None:
        """Retrieve a value from a hash by field"""
        raise NotImplementedError

    @abstractmethod
    async def set_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Set a value in a hash field"""
        raise NotImplementedError

    @abstractmethod
    async def delete_flat_mapping_key(
        self, key: str, field: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Delete a field from a hash"""
        raise NotImplementedError

    @abstractmethod
    async def update_flat_mapping_key(
        self, key: str, field: str, value: Any, *args: Any, **kwargs: Any
    ) -> Any:
        """Update a field in a hash"""
        raise NotImplementedError

    @abstractmethod
    async def get_all_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> dict | Any:
        """Retrieve all fields and values from a hash"""
        raise NotImplementedError

    @abstractmethod
    async def delete_flat_mapping(
        self, key: str, *args: Any, **kwargs: Any
    ) -> Any:
        """Delete a field from a hash"""
        raise NotImplementedError
