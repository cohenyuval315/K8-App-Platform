from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)


class RevocationService:
    def __init__(self, cache: AbstractAsyncCache):
        self._cache = cache
        self.blacklist_tokens = "tokens:blacklist"

    async def on_startup(self):
        await self._cache.create_set(self.blacklist_tokens)

    async def on_shutdown(self):
        await self._cache.delete_set(self.blacklist_tokens)

    def get_token_blacklist_name(self, token: str):
        return f"tokens:blacklist:{token}"

    async def is_token_valid(self, token: str) -> bool:
        # response = await self._cache.set_contains(key=self.blacklist_tokens,value=token)
        name = self.get_token_blacklist_name(token)
        response = await self._cache.get_key(name)
        if response is None:
            return True
        return False

    async def revoke(self, token: str, ttl: int):
        # await self._cache.add_to_set(key=self.blacklist_tokens, value=token)
        # self._cache.set_ttl()
        name = self.get_token_blacklist_name(token)
        await self._cache.set_key(name, token)
        ttl_response = await self._cache.set_ttl(name, ttl)
        return ttl_response
