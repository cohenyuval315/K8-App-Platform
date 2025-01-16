from typing import Annotated, Any

from pydantic import AfterValidator


def port_range(v: Any) -> Any:
    if isinstance(v, str):
        try:
            v = int(v)
        except ValueError:
            assert (
                False
            ), "Port value must be an integer or a string that can be parsed to an integer."

    assert isinstance(v, int), "Port value must be an integer."
    assert 0 <= v < 65535, "Port number must be between 0 and 65534."
    return v


PortType = Annotated[int, AfterValidator(port_range)]
