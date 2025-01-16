from uuid import uuid4
from ssl import SSLContext
from sqlalchemy import Engine, event

ssl_context = SSLContext()

connect_args = {
    "prepared_statement_name_func": lambda: f"__asyncpg_{uuid4()}__",
    "server_settings": {
        "jit": "off",
    },
    "timeout": 0,
    "statement_cache_size": 0,
    "max_cached_statement_lifetime": 0,
    "max_cacheable_statement_size": 0,
    "command_timeout": 0,
    "ssl": ssl_context,
}


def _reset_asyncpg_connection(
    dbapi_connection, connection_record, reset_state
):
    if not reset_state.terminate_only:
        dbapi_connection.execute("CLOSE ALL")
        dbapi_connection.execute("RESET ALL")
        dbapi_connection.execute("DISCARD TEMP")
    dbapi_connection.rollback()


def on_reset_asyncpg_connection(engine: Engine):
    event.listen(engine, "reset", _reset_asyncpg_connection)


def remove_reset_asyncpg_connection(engine: Engine):
    event.remove(engine, "reset", _reset_asyncpg_connection)
