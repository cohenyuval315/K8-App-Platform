import importlib.util
import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Dict, Optional
from uuid import UUID, uuid4

from starlette.datastructures import MutableHeaders

from asgi_correlation_id.context import correlation_id
from pymicroservicesbase.sdk.web_api.core_api.requests.cor_manager import (
    CorrelationIdManager,
)

if TYPE_CHECKING:
    from starlette.types import ASGIApp, Message, Receive, Scope, Send

logger = logging.getLogger("asgi_correlation_id")


def get_libs(libs: list[str]) -> Dict[str, bool]:
    return {
        lib: importlib.util.find_spec("sentry_sdk") is not None for lib in libs
    }


def is_valid_uuid4(uuid_: str) -> bool:
    """
    Check whether a string is a valid v4 uuid.
    """
    try:
        return UUID(uuid_).version == 4
    except ValueError:
        return False


REQUEST_ID_HEADER_KEY = "X-Request-ID"

FAILED_VALIDATION_MESSAGE = "Generated new request ID (%s), since request header value failed validation"


@dataclass
class CorrelationIdMiddleware:
    app: ASGIApp
    manager: CorrelationIdManager
    header_name: str = REQUEST_ID_HEADER_KEY
    update_request_header: bool = True

    # ID-generating callable
    generator: Callable[[], str] = field(default=lambda: uuid4().hex)

    # ID validator
    validator: Optional[Callable[[str], bool]] = field(default=is_valid_uuid4)

    # ID transformer - can be used to clean/mutate IDs
    transformer: Optional[Callable[[str], str]] = field(default=lambda a: a)

    async def __call__(
        self, scope: "Scope", receive: "Receive", send: "Send"
    ) -> None:
        """
        Load request ID from headers if present. Generate one otherwise.
        """
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        headers = MutableHeaders(scope=scope)
        header_value = headers.get(self.header_name.lower())

        validation_failed = False

        if not header_value:
            id_value = self.generator()

        elif self.validator and not self.validator(header_value):
            validation_failed = True
            id_value = self.generator()

        else:
            id_value = header_value

        if self.transformer:
            id_value = self.transformer(id_value)

        if validation_failed is True:
            raise Exception(FAILED_VALIDATION_MESSAGE)
            # self.wsc.logger.warning(FAILED_VALIDATION_MESSAGE, id_value)

        # Update the request headers if needed
        if id_value != header_value and self.update_request_header is True:
            headers[self.header_name] = id_value

        correlation_id.set(id_value)

        self.manager.run_correlation_id(correlation_id)

        async def handle_outgoing_request(message: "Message") -> None:
            if (
                message["type"] == "http.response.start"
                and correlation_id.get()
            ):
                headers = MutableHeaders(scope=message)
                headers.append(self.header_name, correlation_id.get())

            await send(message)

        await self.app(scope, receive, handle_outgoing_request)
        return
