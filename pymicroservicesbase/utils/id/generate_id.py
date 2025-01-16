import uuid


def create_uuid() -> str:
    _id = str(uuid.uuid4())
    _id = _id.replace("-", "")
    return _id


def generate_id(id_length: int = 36):
    unique_id = create_uuid()
    if id_length < len(unique_id):
        raise ValueError("id length must be atleast as big as single uuid")
    while len(unique_id) < id_length:
        unique_id += create_uuid()
    result = unique_id[:id_length]
    if not result:
        raise ValueError("no id was generated")
    return result
