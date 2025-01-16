from enum import Enum


class FilterOptionEnum(Enum):
    """Filter options for FilterParam."""

    EQUAL = "eq"
    NOT_EQUAL = "ne"
    LESS_THAN = "lt"
    LESS_THAN_EQUAL = "le"
    GREATER_THAN = "gt"
    GREATER_THAN_EQUAL = "ge"
    IN = "in"
    NOT_IN = "not_in"
    ANY_EQUAL = "any_eq"
    IS_NONE = "is_none"
