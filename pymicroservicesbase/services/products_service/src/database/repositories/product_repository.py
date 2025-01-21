from typing import Optional


from sqlalchemy.ext.asyncio import AsyncSession

from pymicroservicesbase.services.user_service.src.database.models import User
from pymicroservicesbase.sdk.web_api.common.db.sql.sqlalchemy_repository import (
    SQLAlchemyRepository,
)
import sqlalchemy as sa
from pymicroservicesbase.services.user_service.logger import logger  # noqa


class UserRepository(SQLAlchemyRepository[User]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(User, db_session)

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        stmt = sa.select(User).where(User.id == user_id).limit(1)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def get_user_by_email(self, email: str) -> Optional[User]:
        stmt = sa.select(User).where(User.email == email).limit(1)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> Optional[User]:
        stmt = sa.select(User).where(User.username == username).limit(1)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()
