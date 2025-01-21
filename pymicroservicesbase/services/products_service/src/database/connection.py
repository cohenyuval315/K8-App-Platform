from pymicroservicesbase.sdk.sql import SQLDelegator
from pymicroservicesbase.sdk.sql.engine_factory import EngineFactory

db = SQLDelegator("user_service_db", 60000)

db.engine = EngineFactory().create_engine(
    "postgresql+asyncpg://myuser:mypassword@postgres:5432/mydatabase",
    echo=False,
    pool_pre_ping=True,
    echo_pool=False,
)
