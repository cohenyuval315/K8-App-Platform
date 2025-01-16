import sys
from contextvars import ContextVar, Token
from pymicroservicesbase.sdk.sql.session.session_context import SessionContext
from typing import Generic
from pymicroservicesbase.sdk.sql.session.session_type import SessionType

MIN_VERSION = (3, 7)
if sys.version_info < MIN_VERSION:
    raise RuntimeError(
        f"Python {MIN_VERSION[0]}.{MIN_VERSION[1]} or higher is required. for session context manager (works on both threads and coroutines)"
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}."
    )


class SessionContextManager(Generic[SessionType]):
    """
    Manages the context for database sessions using ContextVar.
    This ensures thread-safe and async-task-safe session handling.
    (pep 567 > python 3.7)
    """

    _session_context: ContextVar[SessionContext[SessionType] | None] = (
        ContextVar("SessionContext", default=None)
    )

    def __init__(self, raise_exceptions: bool = False):
        self.raise_exceptions = raise_exceptions

    def get_session_context(self) -> SessionContext[SessionType] | None:
        """
        Retrieve the current session context for the current task.

        :return: The current session context as a string.
        """
        try:
            return self._session_context.get()
        except LookupError as e:
            if self.raise_exceptions is True:
                raise e
            return None

    def set_session_context(
        self, context: SessionContext[SessionType] | None
    ) -> Token:
        """
        Set a new session context for the current task.

        :param session_id: Unique identifier for the session context.
        :return: A Token that can be used to reset the session context.
        """
        token = self._session_context.set(context)
        return token

    def reset_session_context(self, token: Token) -> None:
        """
        Reset the session context to a previous state.

        :param token: A Token representing the previous session context to restore.
        """
        try:
            self._session_context.reset(token)
        except LookupError as e:
            if self.raise_exceptions is True:
                raise e
                raise ValueError(
                    f"Invalid token provided: {token}. No such session context exists."
                )
            return None
