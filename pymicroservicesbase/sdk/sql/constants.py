from pymicroservicesbase.utils.id.generate_id import generate_id

MODEL_ID_LENGTH = 36


def _generate_unique_id(length: int) -> str:
    _id = generate_id(length)
    return _id


def generate_unique_id() -> str:
    _id = _generate_unique_id(MODEL_ID_LENGTH)
    return _id
