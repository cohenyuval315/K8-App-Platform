from typing import TypeVar

from pymicroservicesbase.sdk.sql.base.base_table import BaseTable


BaseTableType = TypeVar("BaseTableType", bound=BaseTable, covariant=True)
