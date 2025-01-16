from ipaddress import IPv4Address
from typing import Annotated

from pydantic import AfterValidator, HttpUrl

HostUrlType = Annotated[HttpUrl | IPv4Address, AfterValidator(str)]
