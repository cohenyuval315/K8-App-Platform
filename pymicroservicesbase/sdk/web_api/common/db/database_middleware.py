from typing import Any
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp, Receive, Scope, Send


class DatabaseMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        dispatch: DispatchFunction | None = None,
        session_mananger: Any | None = None,
    ) -> None:
        super().__init__(app, dispatch)
        self.session_mananger = session_mananger

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        if self.session_mananger is None:
            raise RuntimeError("session manager must be set")
        session_id = str(uuid4())
        context = self.session_mananger.set_session_context(
            session_id=session_id
        )
        try:
            await self.app(scope, receive, send)
        except Exception as exception:
            raise exception
        finally:
            await self.session_mananger.AsyncScopedSession.close()
            self.session_mananger.reset_session_context(context)
