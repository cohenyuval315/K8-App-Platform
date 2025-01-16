from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy import null


class TenantMixin:
    """Id Mixin Class"""

    __abstract__ = True

    tenant_id: Mapped[str] = mapped_column(String, nullable=True)
