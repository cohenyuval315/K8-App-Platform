from __future__ import annotations

from datetime import date, datetime


# from packages.python.project_core.project_services.sqlalchemy.base.base_table import BaseTable
from pymicroservicesbase.sdk.sql.base.base_table import BaseTable
from pymicroservicesbase.sdk.sql.mixins.id_mixin import IdMixin
from pymicroservicesbase.sdk.sql.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    ForeignKey,
    LargeBinary,
    String,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(BaseTable, IdMixin, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    password_salt: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    first_name: Mapped[str | None] = mapped_column(
        String, nullable=True, default=None
    )
    last_name: Mapped[str | None] = mapped_column(
        String, nullable=True, default=None
    )

    birth_date: Mapped[date | None] = mapped_column(
        Date, nullable=True, default=None
    )

    avatar: Mapped[bytes | None] = mapped_column(
        LargeBinary, nullable=True, default=None
    )  # Store image as BYTEA  | # avatar: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # URL or path
    avatar_url: Mapped[str | None] = mapped_column(
        String, nullable=True, default=None
    )  # Store image as BYTEA  | # avatar: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # URL or path

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None
    )
    last_request: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None
    )
    is_deleted: Mapped[bool | None] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool | None] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool | None] = mapped_column(Boolean, default=False)

    additional_fields: Mapped[dict | None] = mapped_column(
        JSON, nullable=True, default=None
    )

    created_by: Mapped[str | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, default=None
    )
    updated_by: Mapped[str | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, default=None
    )

    created_by_user: Mapped[User | None] = relationship(
        "User",
        foreign_keys=[created_by],
        lazy="select",
        remote_side="User.id",
        # default=None,
    )
    updated_by_user: Mapped[User | None] = relationship(
        "User",
        foreign_keys=[updated_by],
        lazy="select",
        remote_side="User.id",
        # default=None,
    )

    @property
    def full_name(self) -> str | None:
        if self.first_name is not None and self.last_name is not None:
            return (
                f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
            )
        elif self.first_name is not None:
            return f"{self.first_name.capitalize()}"
        elif self.last_name is not None:
            return f"{self.last_name.capitalize()}"
        else:
            return None

    @property
    def age(self) -> int | None:
        if self.birth_date is None:
            return None
        else:
            pass

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
