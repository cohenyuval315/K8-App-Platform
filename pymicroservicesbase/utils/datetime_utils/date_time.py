from datetime import datetime

import pytz


def datetime_to_utc(dt: datetime) -> datetime:
    """
    Converts a datetime object (naive or aware) to UTC and returns a timezone-aware datetime in UTC.

    Parameters:
        dt (datetime): The input datetime object to convert to UTC.

    Returns:
        datetime: Timezone-aware datetime object in UTC.
    """
    if dt.tzinfo is None:
        # If naive, localize to UTC
        dt = pytz.utc.localize(dt)  # Localize to UTC directly
    else:
        # If aware, convert it to UTC
        dt = dt.astimezone(pytz.utc)

    return dt
