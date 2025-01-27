from uuid import UUID


def is_valid_uuid4(uuid_: str) -> bool:
    """
    Check whether a string is a valid v4 uuid.
    """
    try:
        return UUID(uuid_).version == 4
    except ValueError:
        return False
