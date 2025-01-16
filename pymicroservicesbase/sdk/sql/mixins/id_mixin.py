from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pymicroservicesbase.sdk.sql.constants import (
    MODEL_ID_LENGTH,
    generate_unique_id,
)


class IdMixin:
    """Id Mixin Class"""

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(MODEL_ID_LENGTH),
        primary_key=True,
        nullable=False,
        default=generate_unique_id,
    )
