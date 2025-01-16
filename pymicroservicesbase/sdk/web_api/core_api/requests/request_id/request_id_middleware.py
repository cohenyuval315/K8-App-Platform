import uuid

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.sdk.web_api.core_api.requests.exceptions import (
    RequestContextAlreadyExistsError,
)
from pymicroservicesbase.sdk.web_api.core_api.requests.request_id.request_id_context_var import (
    RequestIdContextVar,
)
from pymicroservicesbase.shared.constants.headers import REQUEST_ID_HEADER_KEY


class RequestIdContextMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app
        self.token = None
        self.header_key = REQUEST_ID_HEADER_KEY

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        headers = MutableHeaders(
            scope=scope
        )  # mutable headers from the request scope
        header_value = headers.get(
            self.header_key.lower(), None
        )  # Retrieve the request ID from headers, generate if not present
        existing_ctx = RequestIdContextVar.get(None)
        if existing_ctx is not None:
            raise RequestContextAlreadyExistsError(
                "Request context already exists."
            )

        token = None
        try:
            # Generate a new request ID if not already present in the header
            request_id = header_value if header_value else str(uuid.uuid4())
            token = RequestIdContextVar.set(request_id)

            headers[self.header_key.lower()] = request_id

            # Now proceed to the next ASGI layer (FastAPI or another app)
            async def handle_outgoing_request(message: Message) -> None:
                """Handle response and ensure the request ID is added to the response headers."""
                if message["type"] == "http.response.start":
                    # Add request ID to the response headers
                    response_headers = MutableHeaders(scope=message)
                    response_headers.append(self.header_key, request_id)

                # Forward the message to the next layer in the ASGI pipeline
                await send(message)

            await self.app(scope, receive, handle_outgoing_request)

        except WebServiceError as e:
            raise e
        finally:
            # Always clean up by resetting the context variable after the request is processed
            if token is not None:
                RequestIdContextVar.reset(token)
