from typing import Dict
from contextvars import Token
from pymicroservicesbase.sdk.sql.session.session_context import SessionContext


class SessionContextRegistry:
    """
    Manages multiple session contexts by token.
    Keeps track of all session contexts across tasks/threads.
    """

    _contexts: Dict[Token, SessionContext] = {}

    @classmethod
    def get_context_by_token(cls, token: Token) -> SessionContext | None:
        """
        Retrieve a session context using its token.
        Returns None if no context is associated with the token.
        """
        return cls._contexts.get(token)

    @classmethod
    def set_context(cls, context: SessionContext) -> Token:
        """
        Set a new session context and return the associated token.
        """
        token = context.get_token()
        cls._contexts[token] = context
        return token

    @classmethod
    def reset_context(cls, token: Token) -> None:
        """
        Reset and remove a session context associated with the provided token.
        """
        if token not in cls._contexts:
            raise ValueError(f"Invalid token: {token}")

        cls._contexts.pop(token)
