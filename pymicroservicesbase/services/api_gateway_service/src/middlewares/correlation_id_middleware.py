import uuid

from starlette.datastructures import MutableHeaders

from pymicroservicesbase.sdk.web_api.core_api.correlation.correlation_id_context_var import (
    CorrelationIdContextVar,
)
from pymicroservicesbase.services.api_gateway_service.logger import logger
from pymicroservicesbase.shared.constants.headers import (
    CORRELATION_ID_HEADER_KEY,
)


class CorrelationIdMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        correlation_id = CorrelationIdContextVar.get()
        if correlation_id is not None:
            logger.warning(
                f"correlation id should not exists: {correlation_id}"
            )
        correlation_id = str(uuid.uuid4())
        token = CorrelationIdContextVar.set(correlation_id)
        try:
            headers = MutableHeaders(scope=scope)
            headers.append(CORRELATION_ID_HEADER_KEY, correlation_id)
            scope["headers"] = headers.raw

            await self.app(scope, receive, send)
        finally:
            CorrelationIdContextVar.reset(token)
