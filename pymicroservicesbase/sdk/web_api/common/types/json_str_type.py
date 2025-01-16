import json
from typing import Annotated

from pydantic import AfterValidator


def valid_json(v: str):
    """_summary_

    Args:
        v (str): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    try:
        assert isinstance(v, str), "value must be string"
        value = json.loads(v)
        assert isinstance(value, dict), "value must be a valid json"
    except json.JSONDecodeError as e:
        raise ValueError(
            "Value must be a valid JSON string or a dictionary"
        ) from e
    return v


JsonStrType = Annotated[str, AfterValidator(valid_json)]
