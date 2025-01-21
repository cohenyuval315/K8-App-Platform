from __future__ import annotations



# from packages.python.project_core.project_services.sqlalchemy.base.base_table import BaseTable
from pymicroservicesbase.sdk.sql.base.base_table import BaseTable
from pymicroservicesbase.sdk.sql.mixins.id_mixin import IdMixin
from pymicroservicesbase.sdk.sql.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy import (
    JSON,
    Boolean,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column


class Product(BaseTable, IdMixin, TimestampMixin):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String, unique=True, index=True)

    is_deleted: Mapped[bool | None] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool | None] = mapped_column(Boolean, default=True)

    config: Mapped[dict | None] = mapped_column(
        JSON, nullable=True, default=None
    )

    created_by: Mapped[str | None] = mapped_column(
        String, nullable=True, default=None
    )
    updated_by: Mapped[str | None] = mapped_column(
        String, nullable=True, default=None
    )

    def __repr__(self):
        return f"<Product(id={self.id}, title={self.title})>"
