from typing import Annotated

from fastapi import Depends
from .web_service import WebService
import time
import datetime
from pymicroservicesbase.utils.datetime_utils.date_time import datetime_to_utc


class WebServiceContainer:
    def __init__(
        self,
        web_service: WebService,
        config,
        db=None,
    ):
        self._web_service = web_service
        self._config = config
        self._db = db
        self._start_time = time.time()
        self._start_datetime = datetime_to_utc(datetime.datetime.now())

    def get_web_service(self) -> WebService:
        return self._web_service


def get_web_service_container():
    return WebServiceContainer


WebServiceContainerDep = Annotated[
    WebServiceContainer, Depends(get_web_service_container)
]
