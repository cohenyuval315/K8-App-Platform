from contextlib import asynccontextmanager
from functools import wraps
from typing import Any, Callable, Dict, Type

from sqlalchemy import MetaData, event, exc, text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from pymicroservicesbase.sdk.sql.base.base_table import BaseTable

# from pymicroservicesbase.sdk.sql.engine import create_engine
from pymicroservicesbase.sdk.sql.exceptions import (
    NotConfiguratedSQLDelegatorError,
    SessionAlreadyExistsInAsyncContextError,
)
from pymicroservicesbase.sdk.sql.session.session_context import SessionContext
from pymicroservicesbase.sdk.sql.session.session_context_manager import (
    SessionContextManager,
)
from pymicroservicesbase.shared.logging import logger
from pymicroservicesbase.utils.timeout.timeout import Timeout


class SQLDelegator:
    def __init__(self, name: str, session_timeout: int, **kwargs: Any):
        self._name: str = name
        self._ctx: SessionContextManager = SessionContextManager()
        self._SessionClass = AsyncSession
        self._engine: AsyncEngine | None = None
        self._base_table_class: Type[BaseTable] = BaseTable
        self._session_event_listeners = None
        self._timeout = session_timeout
        self._execution_options = None
        self._kwargs = kwargs

    @property
    def metadata(self) -> MetaData:
        return self._base_table_class.metadata

    @property
    def registery(self) -> Any:
        return self._base_table_class.registry

    @property
    def is_configured(self):
        return self._SessionClass is not None

    async def dispose_all(self):
        if self._engine:
            await self._engine.dispose(close=True)

    @property
    def engine(self) -> AsyncEngine | None:
        return self._engine

    @engine.setter
    def engine(self, engine: AsyncEngine):
        self._ctx.set_session_context(None)
        if self._engine is not None:

            def reset_connection(dbapi_connection, record):
                if not dbapi_connection:
                    return
                dbapi_connection.rollback()

            event.listen(engine.sync_engine, "reset", reset_connection)
        self._engine = engine

    async def on_session_commit(self):
        pass

    async def on_session_close(self):
        pass

    async def on_session_error(self):
        pass

    async def on_session_rollback(self):
        pass

    @asynccontextmanager
    async def with_engine(self):
        if self._engine is None:
            raise NotConfiguratedSQLDelegatorError()
        try:
            yield self._engine
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            await self._engine.dispose(close=False)

    async def ping(self):
        async with self.with_connection() as conn:
            res = await conn.execute(text("SELECT 1"))
            return res

    @asynccontextmanager
    async def with_connection(self):
        async with self.with_engine() as engine:
            async with engine.connect() as conn:
                try:
                    yield conn
                except Exception as e:
                    logger.error(e)
                    raise e
                finally:
                    await conn.close()

    def transactional(self, *session_args, **session_kwargs):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                async with self.transaction(*session_args, **session_kwargs):
                    res = await func(*args, **kwargs)
                    return res

            return wrapper

        return decorator

    def sessional(self, *session_args, **session_kwargs):
        async def decorator(self, func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                async with self.session(*session_args, **session_kwargs):
                    return func(*args, **kwargs)

            return wrapper

        return decorator

    @asynccontextmanager
    async def two_phase_transaction(self, *args, **kwargs):
        async with self.transaction(*args, **kwargs) as session:
            session.sync_session.prepare()
            yield session

    @asynccontextmanager
    async def transaction(self, *args, **kwargs):
        async with self.session(*args, **kwargs) as session:
            if session.in_transaction():
                yield session
            else:
                async with session.begin():
                    yield session

    @asynccontextmanager
    async def session(
        self,
        expunge: bool = False,
        event_listeners: Dict[str, Callable] | None = None,
        *arg: Any,
        **kwargs: Any,
    ):
        session_ctx = self._ctx.get_session_context()
        if session_ctx is not None:
            yield session_ctx.get_session()
        else:
            async with self._create_session(*arg, **kwargs) as session:
                # _attach_session_event_listeners(session, event_listeners)
                try:
                    with Timeout(self._timeout):
                        yield session
                        if expunge:
                            session.expunge_all()
                except exc.TimeoutError:
                    raise TimeoutError("expired")
                # except Exception as e:
                #     raise e
                # except exc.InvalidRequestError as e:
                #     pass
                # except exc.DBAPIError as e:
                #     pass
                # except exc.TimeoutError:
                #     pass
                # except Exception as e:
                #     pass
                # else:
                #     pass
                # finally:
                #     pass
                # _detach_session_event_listeners(session, event_listeners)

    @asynccontextmanager
    async def _create_session(
        self, commit_nested: bool = False, *args: Any, **kwargs: Any
    ):
        if not self.is_configured:
            raise NotConfiguratedSQLDelegatorError()

        if self._ctx.get_session_context() is not None:
            raise SessionAlreadyExistsInAsyncContextError()

        session = self._SessionClass(bind=self._engine, *args, **kwargs)
        sc = SessionContext(session)
        token = self._ctx.set_session_context(sc)
        sc.set_token(token)

        try:
            yield session

            if session.sync_session.in_transaction() or (
                commit_nested and session.sync_session.in_nested_transaction()
            ):
                await session.commit()

        except Exception as e:
            await session.rollback()
            await self.on_session_rollback()
            await self.on_session_error()
            raise e
        else:
            await self.on_session_commit()
        finally:
            await session.close()
            self._ctx.reset_session_context(token)
            await self.on_session_close()

    async def transactionalism(self, *session_args, **session_kwargs):
        async def decorator(self, func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                async with self.transaction_recursive(
                    *session_args, **session_kwargs
                ):
                    return func(*args, **kwargs)

            return wrapper

        return decorator

    @asynccontextmanager
    async def transaction_recursive(self, *args, **kwargs):
        """
        Begin a transaction checkpoint and nest transactions if applicable.
        Recursively creates nested transactions as long as the session is already in a transaction.
        """
        async with self.session(*args, **kwargs) as session:
            if session.in_transaction():
                async with session.begin_nested() as nested_session:
                    yield await self._nest_transaction(nested_session)
            else:
                async with session.begin():
                    yield session

    async def _nest_transaction(self, session):
        """
        Recursively creates nested transactions as long as the session is in a transaction.
        """
        if session.in_transaction():
            async with session.begin_nested() as nested_session:
                return await self._nest_transaction(nested_session)
        else:
            return session
