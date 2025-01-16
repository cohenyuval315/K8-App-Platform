from datetime import datetime, timezone
from .date_time import datetime_to_utc


def datetime_to_string(dt: datetime) -> str:
    """
    Converts a datetime object to an UTC ISO 8601 formatted string.

    Parameters:
        dt (datetime): The input datetime to convert.

    Returns:
        str: The ISO 8601 formatted string.
    """
    dt = datetime_to_utc(dt=dt)
    return dt.isoformat()


def string_to_datetime(dt_str: str) -> datetime:
    """
    Converts an ISO 8601 formatted string to a datetime object.

    Parameters:
        dt_str (str): The ISO 8601 formatted string to convert.

    Returns:
        datetime: The corresponding datetime object.
    """
    dt = datetime.fromisoformat(dt_str)
    return dt


def datetime_to_timestamp(dt: datetime) -> float:
    """
    Convert a datetime object to a Unix timestamp (seconds since the epoch).
    The datetime is assumed to be in UTC.

    :param dt: The datetime object to convert.
    :return: A Unix timestamp (float).
    """
    # Ensure datetime is in UTC and convert to timestamp
    return datetime_to_utc(dt=dt).timestamp()


def timestamp_to_datetime(timestamp: float) -> datetime:
    """
    Convert a Unix timestamp (seconds since the epoch) to a datetime object.
    The resulting datetime will be in UTC.

    :param timestamp: The Unix timestamp to convert.
    :return: A datetime object in UTC.
    """

    return datetime.fromtimestamp(timestamp, timezone.utc)


def string_to_timestamp(date_str: str) -> float:
    """
    Convert a date/time string to a Unix timestamp (seconds since the epoch).
    Assumes the string represents UTC time.

    :param date_str: The date/time string to convert.
    :return: A Unix timestamp (float).
    """
    dt = string_to_datetime(date_str)
    timestamp = datetime_to_timestamp(dt)
    return timestamp


def timestamp_to_string(timestamp: float) -> str:
    """
    Convert a Unix timestamp (seconds since the epoch) to a formatted string.
    The output string will be in UTC.

    :param timestamp: The Unix timestamp to convert.
    :return: A formatted string representing the UTC timestamp.
    """
    dt = timestamp_to_datetime(timestamp)
    date_string = datetime_to_string(dt)
    return date_string


def datetime_to_unix(dt: datetime) -> int:
    """Convert a datetime object to a UNIX timestamp."""
    _dt = datetime_to_utc(dt)
    return int(_dt.timestamp())


def unix_to_datetime(ts: int) -> datetime:
    """Convert a UNIX timestamp to a datetime object."""
    dt = datetime.fromtimestamp(ts)
    return datetime_to_utc(dt)
