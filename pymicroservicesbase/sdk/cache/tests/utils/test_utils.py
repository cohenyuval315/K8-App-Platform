from typing import List, Tuple
from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)
from pymicroservicesbase.sdk.cache.tests.utils.generate import (
    generate_test_key,
    generate_test_string,
)


async def _set_random_cache_key_value(
    cache: AbstractAsyncCache,
) -> Tuple[str, str]:
    key = generate_test_key()
    value = generate_test_string()
    await cache.set_key(key, value)
    return key, value


async def _set_random_cache_keys_values(
    cache: AbstractAsyncCache, size: int = 1
) -> List[Tuple[str, str]]:
    results = []
    for _ in range(size):
        key = generate_test_key()
        value = generate_test_string()
        await cache.set_key(key, value)
        results.append((key, value))
    return results
