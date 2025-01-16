from .conversion import datetime_to_utc
import datetime


def utcnow() -> datetime.datetime:
    return datetime_to_utc(datetime.datetime.now())
