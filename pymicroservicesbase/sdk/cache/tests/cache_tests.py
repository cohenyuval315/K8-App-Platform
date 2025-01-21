from typing import Any, Generator
import pytest
import asyncio

import pytest_asyncio


from pymicroservicesbase.sdk.cache.in_memory_async_cache import (
    InMemoryAsyncCache,
)
from pymicroservicesbase.sdk.cache.redis_async_cache import RedisAsyncCache

from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)
from .utils.generate import (
    generate_test_key,
    generate_random_key,
    generate_test_string,
    generate_test_flat_mapping,
    generate_test_ttl,
)
from .utils.test_utils import (
    _set_random_cache_key_value,
)

TTL_LEEWAY = 5


def is_within_leeway(ttl_a: float, ttl_b: float) -> bool:
    return abs(ttl_a - ttl_b) < TTL_LEEWAY


@pytest.fixture(scope="session", autouse=True)
def event_loop() -> Generator["asyncio.AbstractEventLoop", Any, None]:
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def redis_cache(event_loop):
    """Fixture to provide InMemoryAsyncCache instance."""
    cache = RedisAsyncCache()
    await cache.connect()
    yield cache
    await cache.close()


@pytest_asyncio.fixture
async def in_memory_cache():
    """Fixture to provide InMemoryAsyncCache instance."""
    cache = InMemoryAsyncCache()
    await cache.connect()
    yield cache
    await cache.close()


# @pytest.mark.parametrize(
#     "cache", ["in_memory_cache"],indirect=True)
@pytest_asyncio.fixture
async def cache(in_memory_cache, redis_cache):
    """Fixture to provide InMemoryAsyncCache instance."""
    yield redis_cache


# Key Operations
async def test_get_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)
    result = await cache.get_key(key)
    assert result == value, f"Expected {value}, but got {result}"


async def test_set_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)
    result = await cache.get_key(key)
    assert result == value, f"Expected {value}, but got {result}"


async def test_delete_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)
    await cache.delete_key(key)
    result = await cache.get_key(key)
    assert result is None, "Key should be deleted and result should be None"


async def test_delete_keys(cache: AbstractAsyncCache):
    keys = [generate_test_key() for _ in range(3)]
    for key in keys:
        await cache.set_key(key, generate_test_string())
    await cache.delete_keys(keys)
    for key in keys:
        result = await cache.get_key(key)
        assert (
            result is None
        ), f"Key {key} should be deleted and result should be None"


async def test_get_keys(cache: AbstractAsyncCache):
    keys = [generate_test_key() for _ in range(3)]
    values = [generate_test_string() for _ in range(3)]
    for key, value in zip(keys, values):
        await cache.set_key(key, value)
    result = await cache.get_keys(keys)
    assert result == values, f"Expected values {values}, but got {result}"


async def test_key_exists(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)
    result = await cache.key_exists(key)
    assert result is True, "Key should exist"


async def test_get_ttl(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)

    ttl = generate_test_ttl()
    await cache.set_ttl(key, ttl)

    result = await cache.get_ttl(key)

    assert is_within_leeway(
        result, ttl
    ), f"Expected TTL {ttl}, but got {result}"


async def test_set_ttl(cache: AbstractAsyncCache):
    ttl = generate_test_ttl()
    key, _ = await _set_random_cache_key_value(cache)
    await cache.set_ttl(key, ttl)
    result = await cache.get_ttl(key)
    assert is_within_leeway(
        result, ttl
    ), f"Expected TTL {ttl}, but got {result}"


async def test_remove_ttl(cache: AbstractAsyncCache):
    key, _ = await _set_random_cache_key_value(cache)
    ttl = generate_test_ttl()
    await cache.set_ttl(key, ttl)
    ttl = await cache.get_ttl(key)
    assert ttl is not None, "ttl is not created"

    await cache.remove_ttl(key)
    result = await cache.get_ttl(key)
    assert result is None, "TTL should be removed"


# Set Operations


async def test_create_set(cache: AbstractAsyncCache):
    key = generate_test_key()
    await cache.create_set(key)
    result = await cache.get_set_size(key)
    assert result == 0, "New set should be empty"


async def test_add_to_set(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.add_to_set(key, value)
    result = await cache.get_set_size(key)
    assert result > 0, "Set should have added value"


async def test_remove_from_set(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.create_set(key)
    await cache.add_to_set(key, value)
    await cache.remove_from_set(key, value)
    result = await cache.get_set_size(key)
    assert result == 0, "Set should be empty after removal"


async def test_delete_set(cache: AbstractAsyncCache):
    key = generate_test_key()
    await cache.create_set(key)
    await cache.delete_set(key)
    result = await cache.get_set_size(key)
    assert result <= 0, "Set should be deleted"


async def test_get_set_size(cache: AbstractAsyncCache):
    key = generate_test_key()
    await cache.create_set(key)
    await cache.add_to_set(key, generate_test_string())
    result = await cache.get_set_size(key)
    assert result > 0, "Set size should be greater than 0 after adding"


async def test_set_contains(cache: AbstractAsyncCache):
    key = generate_test_key()
    value = generate_test_string()
    await cache.create_set(key)
    await cache.add_to_set(key, value)
    result = await cache.set_contains(key, value)
    assert result is True, "Set should contain the added value"


# async def test_get_random_member_from_set(cache: AbstractAsyncCache):
#     set_key = generate_test_key()
#     value = generate_test_string()
#     await cache.create_set(set_key)
#     await cache.add_to_set(set_key, value)
#     result = await cache.get_random_member_from_set(set_key)
#     assert result == value, f"Expected {value}, but got {result}"


# async def test_pop_random_member_from_set(cache: AbstractAsyncCache):
#     key = generate_test_key()
#     value = generate_test_string()
#     await cache.create_set(key)
#     await cache.add_to_set(key, value)
#     result = await cache.pop_random_member_from_set(key)
#     assert result == value, f"Expected {value}, but got {result}"


# async def test_get_multiple_randoms_members_from_set(cache: AbstractAsyncCache):
#     key = generate_test_key()
#     values = [generate_test_string() for _ in range(3)]
#     await cache.create_set(key)
#     for value in values:
#         await cache.add_to_set(key, value)
#     result = await cache.get_multiple_randoms_members_from_set(key, 3)
#     assert len(result) == 3, "Expected 3 random members"
#     assert all(v in values for v in result), "All random members should be from the set"

# Mapping Operations


async def test_set_flat_mapping(cache: AbstractAsyncCache):
    key = generate_test_key()
    mapping = generate_test_flat_mapping()
    await cache.set_flat_mapping(key, mapping)
    result = await cache.get_all_flat_mapping(key)
    assert result == mapping, f"Expected mapping {mapping}, but got {result}"


async def test_get_flat_mapping_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    mapping = generate_test_flat_mapping()
    field, value = list(mapping.items())[0]
    await cache.set_flat_mapping(key, mapping)
    result = await cache.get_flat_mapping_key(key, field)
    assert result == value, f"Expected value {value}, but got {result}"


async def test_set_flat_mapping_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    field = generate_random_key()
    value = generate_test_string()
    await cache.set_flat_mapping_key(key, field, value)
    result = await cache.get_flat_mapping_key(key, field)
    assert result == value, f"Expected value {value}, but got {result}"


async def test_delete_flat_mapping_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    field = generate_random_key()
    value = generate_test_string()
    await cache.set_flat_mapping_key(key, field, value)
    await cache.delete_flat_mapping_key(key, field)
    result = await cache.get_flat_mapping_key(key, field)
    assert result is None, f"Field {field} should be deleted"


async def test_update_flat_mapping_key(cache: AbstractAsyncCache):
    key = generate_test_key()
    field = generate_random_key()
    value = generate_test_string()
    new_value = generate_test_string()
    await cache.set_flat_mapping_key(key, field, value)
    await cache.update_flat_mapping_key(key, field, new_value)
    result = await cache.get_flat_mapping_key(key, field)
    assert result == new_value, f"Expected {new_value}, but got {result}"


async def test_delete_flat_mapping(cache: AbstractAsyncCache):
    key = generate_test_key()
    mapping = generate_test_flat_mapping()
    await cache.set_flat_mapping(key, mapping)
    await cache.delete_flat_mapping(key)
    result = await cache.get_all_flat_mapping(key)
    assert result is None, f"Mapping for {key} should be deleted"
