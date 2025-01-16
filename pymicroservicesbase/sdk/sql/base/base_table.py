from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from pymicroservicesbase.sdk.sql.mixins.id_mixin import IdMixin


class BaseTable(DeclarativeBase, AsyncAttrs, IdMixin):
    """ """

    __abstract__ = True
    __table_args__ = {}
    __mapper_args__ = {
        "eager_defaults": True,
        "batch": True,
    }
