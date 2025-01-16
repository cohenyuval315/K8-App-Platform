# utils/datetime/formats.py

import enum
from datetime import datetime
from typing import Optional

from .conversion import string_to_datetime


class DateTimeFormat(str, enum.Enum):
    """Enum to define standard date and time formats"""

    # Date Formats
    DATE_ISO = "%Y-%m-%d"  # ISO format: 2024-11-17
    DATE_US = "%m/%d/%Y"  # US format: 11/17/2024
    DATE_EU = "%d/%m/%Y"  # European format: 17/11/2024

    # Time Formats
    TIME_24HR = "%H:%M:%S"  # 24-hour format: 15:30:45
    TIME_12HR = "%I:%M:%S %p"  # 12-hour format with AM/PM: 03:30:45 PM
    TIME_24HR_MS = (
        "%H:%M:%S.%f"  # 24-hour format with milliseconds: 15:30:45.123
    )
    TIME_12HR_MS = "%I:%M:%S.%f %p"  # 12-hour format with milliseconds and AM/PM: 03:30:45.123 PM

    # Datetime Formats
    DATETIME_ISO = "%Y-%m-%d %H:%M:%S"  # ISO format with time
    DATETIME_US = "%m/%d/%Y %I:%M %p"  # US format with time
    DATETIME_EU = "%d/%m/%Y %H:%M:%S"  # European format with time
    DATETIME_ISO_MS = "%Y-%m-%d %H:%M:%S.%f"  # ISO format with milliseconds
    DATETIME_US_MS = (
        "%m/%d/%Y %I:%M:%S.%f %p"  # US format with time and milliseconds
    )
    DATETIME_EU_MS = (
        "%d/%m/%Y %H:%M:%S.%f"  # European format with time and milliseconds
    )

    # DateTime with Timezone
    DATETIME_TZ_ISO = "%Y-%m-%d %H:%M:%S%z"  # ISO format with timezone
    DATETIME_TZ_US = "%m/%d/%Y %I:%M %p %z"  # US format with timezone
    DATETIME_TZ_EU = "%d/%m/%Y %H:%M:%S %z"  # European format with timezone
    DATETIME_TZ_ISO_MS = (
        "%Y-%m-%d %H:%M:%S.%f%z"  # ISO with milliseconds and timezone
    )
    DATETIME_TZ_US_MS = (
        "%m/%d/%Y %I:%M:%S.%f %p %z"  # US with milliseconds and timezone
    )
    DATETIME_TZ_EU_MS = (
        "%d/%m/%Y %H:%M:%S.%f %z"  # EU with milliseconds and timezone
    )


def format_datetime_string(
    dt_str: str,
    target_format: DateTimeFormat,
    current_format: Optional[DateTimeFormat] = None,
) -> str:
    """
    Converts a date string from one format to another.

    :param date_str: The date string to convert.
    :param target_format: The format to convert the string to.
    :param current_format: The format of the input string. default iso
    :return: The date string in the target format.
    """
    if current_format is None:
        dt = string_to_datetime(dt_str)
    else:
        dt = datetime.strptime(dt_str, current_format.value)
    formatted_date = dt.strftime(target_format.value)
    return formatted_date
