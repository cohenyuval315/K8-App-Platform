import asyncio
from pymicroservicesbase.sdk.cache.abstract_async_cache import (
    AbstractAsyncCache,
)
from pymicroservicesbase.utils.datetime_utils.conversion import (
    datetime_to_string,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.services.authentication_service.logger import logger


class UserActiveSessionService:
    def __init__(self, cache: AbstractAsyncCache):
        self.cache = cache
        self.online_users_key = "online"

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    async def create_user_session(
        self,
        session_key: str,
        user_set_key: str,
        value: dict,
        expire_at: int,
        product_set_key: str | None = None,
    ):
        """Create a new user session and add it to the global user session set and product's active session set."""
        logger.debug(f"Creating user session: {session_key}")

        session_create = await self.cache.set_flat_mapping(session_key, value)
        logger.debug(
            f"Cache response for set_hash for {session_key}: {session_create}"
        )

        session_expire = await self.cache.set_ttl(session_key, expire_at)
        logger.debug(
            f"Cache response for set_expire for {session_key}: {session_expire}"
        )

        user_set = await self.cache.add_to_set(
            key=user_set_key, value=session_key
        )
        logger.debug(
            f"Cache response for add_to_set for {user_set_key}: {user_set}"
        )

        if product_set_key is not None:
            product_set = await self.cache.add_to_set(
                key=product_set_key, value=session_key
            )
            logger.debug(
                f"Cache response for add_to_set for {product_set_key}: {product_set}"
            )

            await self.cache.add_to_set(
                key=self.online_users_key, value=session_key
            )

    async def update_user_session_expire(self, session_key: str, seconds: int):
        """Update the TTL for an existing session."""
        logger.debug(
            f"Updating expiration for session: {session_key} by {seconds} seconds"
        )

        exists = await self.cache.key_exists(session_key)
        logger.debug(f"Cache response for exists for {session_key}: {exists}")

        if exists:
            dt = utcnow()
            await self.cache.set_flat_mapping_key(
                session_key, "last_activity", datetime_to_string(dt)
            )
            await self.cache.set_flat_mapping_key(
                session_key, "extend_count", 1
            )
            session_expire = await self.cache.set_ttl(session_key, seconds)
            logger.debug(
                f"Cache response for set_expire for {session_key}: {session_expire}"
            )
            return True
        logger.warning(f"Session not found for session_key: {session_key}")
        return False

    async def update_user_session(self, session_key: str, value):
        """Update the TTL for an existing session."""
        logger.debug(f"Updating user session: {session_key} with new value.")
        res = await self.cache.set_flat_mapping(session_key, value)
        logger.debug(
            f"Cache response for update_hash for {session_key}: {res}"
        )
        return res

    async def _delete_user_session(
        self,
        session_key: str,
        user_set_key: str,
        product_set_key: str | None = None,
    ):
        """Delete a user session."""
        logger.debug(f"Deleting user session: {session_key}")

        delete_session = await self.cache.delete_key(session_key)
        logger.debug(
            f"Cache response for delete_key for {session_key}: {delete_session}"
        )

        user_set_length = await self.cache.get_set_size(user_set_key)
        logger.debug(
            f"Cache response for get_set_length for {user_set_key}: {user_set_length}"
        )
        if user_set_length > 0:
            await self.cache.remove_from_set(user_set_key, session_key)
            logger.debug(
                f"Cache response for remove_from_set for {user_set_key}: {session_key}"
            )
            user_set_length -= 1

        if user_set_length == 0:
            delete_user_set = await self.cache.delete_key(user_set_key)
            logger.debug(
                f"Cache response for delete_key for user set {user_set_key}: {delete_user_set}"
            )

        if product_set_key is not None:
            product_set_length = await self.cache.get_set_size(product_set_key)
            logger.debug(
                f"Cache response for get_set_length for {product_set_key}: {product_set_length}"
            )
            if product_set_length > 0:
                await self.cache.remove_from_set(product_set_key, session_key)
                logger.debug(
                    f"Cache response for remove_from_set for {product_set_key}: {session_key}"
                )
                product_set_length -= 1

            if product_set_length == 0:
                delete_product_set = await self.cache.delete_key(
                    product_set_key
                )
                logger.debug(
                    f"Cache response for delete_key for product set {product_set_key}: {delete_product_set}"
                )

    async def delete_user_session(self, session_key: str):
        return await self.cache.delete_key(session_key)

    async def delete_empty_user_sessions(self, user_set_key: str):
        user_set_length = await self.cache.get_set_size(user_set_key)
        if user_set_length == 0:
            delete_user_set = await self.cache.delete_key(user_set_key)
            logger.debug(
                f"Cache response for delete_key for user set {user_set_key}: {delete_user_set}"
            )

    async def delete_user_session_from_user_sessions(
        self, session_key: str, user_set_key: str
    ):
        return await self.cache.remove_from_set(user_set_key, session_key)

    async def delete_user_session_from_product_sessions(
        self, session_key: str, product_set_key: str
    ):
        return await self.cache.remove_from_set(product_set_key, session_key)

    async def get_user_session(self, session_key: str):
        logger.debug(f"Retrieving user session for session_key: {session_key}")
        session = await self.cache.get_all_flat_mapping(session_key)
        logger.debug(
            f"Cache response for get_all_hash_keys for {session_key}: {session}"
        )
        return session

    async def get_user_session_expire(self, session_key: str):
        logger.debug(f"Getting expiration for session: {session_key}")
        expire_time = await self.cache.get_ttl(session_key)
        logger.debug(
            f"Cache response for get_expire for {session_key}: {expire_time}"
        )
        return expire_time

    async def get_user_sessions_ids(self, user_set_key: str):
        logger.debug(
            f"Retrieving user sessions IDs for user set key: {user_set_key}"
        )
        set_members = await self.cache.get_set_members(user_set_key)
        logger.debug(
            f"Cache response for get_set for {user_set_key}: {set_members}"
        )
        return set_members

    async def get_user_sessions(self, user_set_key: str):
        logger.debug(
            f"Retrieving user sessions for user set key: {user_set_key}"
        )
        set_members = await self.cache.get_set_members(user_set_key)
        logger.debug(
            f"Cache response for get_set for {user_set_key}: {set_members}"
        )
        tasks = [
            self.cache.get_all_flat_mapping(member) for member in set_members
        ]
        result = await asyncio.gather(*tasks)
        logger.debug(
            f"Cache response for get_all_hash_keys for user set {user_set_key}: {result}"
        )
        return result

    async def get_product_sessions_ids(self, product_set_key: str):
        logger.debug(
            f"Retrieving product sessions IDs for product set key: {product_set_key}"
        )
        set_members = await self.cache.get_set_members(product_set_key)
        logger.debug(
            f"Cache response for get_set for {product_set_key}: {set_members}"
        )
        return set_members

    async def get_product_sessions(self, product_set_key: str):
        logger.debug(
            f"Retrieving product sessions for product set key: {product_set_key}"
        )
        set_members = await self.cache.get_set_members(product_set_key)
        logger.debug(
            f"Cache response for get_set for {product_set_key}: {set_members}"
        )
        tasks = [
            self.cache.get_all_flat_mapping(member) for member in set_members
        ]
        result = await asyncio.gather(*tasks)
        logger.debug(
            f"Cache response for get_all_hash_keys for product set {product_set_key}: {result}"
        )
        return result

    async def delete_all_product_sessions(self, product_set_key: str):
        logger.debug(
            f"Deleting all product sessions for product set key: {product_set_key}"
        )
        result = await self.cache.delete_key(product_set_key)
        logger.debug(
            f"Cache response for delete_key for product set {product_set_key}: {result}"
        )
        return result

<<<<<<< Updated upstream

    async def get_online_users_sessions_ids(self):
        sessions = await self.cache.get_set_members(self.online_users_key)
        return sessions

    async def get_online_users_sessions(self):
        sessions_ids = await self.get_online_users_sessions_ids()
        # sessions_ids
        # asyncio.gather()

    async def delete_user_session_from_online(
        self, session_key: str
    ):
        return await self.cache.remove_from_set(self.online_users_key, session_key)
=======
    async def get_online_users_sessions_ids(self):
        sessions = await self.cache.get_set_members(self.online_users_key)
        return sessions

    async def get_online_users_sessions(self):
        sessions_ids = await self.get_online_users_sessions_ids()
        # sessions_ids
        # asyncio.gather()

    async def delete_user_session_from_online(self, session_key: str):
        return await self.cache.remove_from_set(
            self.online_users_key, session_key
        )
>>>>>>> Stashed changes
