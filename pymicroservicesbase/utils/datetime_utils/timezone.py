from __future__ import annotations

import time

import datetime as dt

import pytz

from .conversion import timestamp_to_datetime

UTC = pytz.UTC


def is_timezone_aware(value: dt.datetime) -> bool:
    return value.utcoffset() is not None


def is_not_timezone_aware(value: dt.datetime) -> bool:
    return value.utcoffset() is None


def utcnow() -> dt.datetime:
    """Get the current date and time in UTC."""
    return dt.datetime.now(tz=UTC)


def get_local_timezone():
    """
    Returns:
        timezone: timezone string
    """
    tz = pytz.timezone(time.tzname[0])
    return tz


def convert_datetime_timezone(
    dt: dt.datetime, timezone: str | None = None
) -> dt.datetime:
    """
    Converts a datetime object (naive or aware) to the specified timezone and returns a timezone-aware datetime.

    Parameters:
        dt (datetime): The input datetime object to convert to the specified timezone.
        timezone (str): The name of the target timezone (e.g., "America/New_York", "Europe/London").

    Returns:
        datetime: Timezone-aware datetime object in the specified timezone.
    """

    if timezone is None:
        # Default to machine's local timezone
        tz = get_local_timezone()
    else:
        tz = pytz.timezone(timezone)  # Get the timezone object\

    if dt.tzinfo is None:
        # If naive, localize to the specified local timezone
        dt = tz.localize(dt)  # Localize to the desired timezone
    else:
        # If aware, convert it to the local timezone
        dt = dt.astimezone(tz)
    return dt


def convert_timestamp_timezone(
    timestamp: float, target_timezone: str
) -> dt.datetime:
    """
    Convert a Unix timestamp to a datetime object in the specified target timezone.

    :param timestamp: The Unix timestamp to convert.
    :param target_timezone: The target timezone (e.g., 'US/Eastern', 'Europe/London').
    :return: A datetime object in the target timezone.
    """
    dt_utc = timestamp_to_datetime(timestamp)
    target_tz = pytz.timezone(target_timezone)
    dt_target = dt_utc.astimezone(target_tz)
    return dt_target
