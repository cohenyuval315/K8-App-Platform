from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

# from pymicroservicesbase.sdk.web_api.common.db.sql.session_dep import _SessionDep
from pymicroservicesbase.services.user_service.src.database.connection import (
    db,
)


async def get_session():
    async with db.session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
