from contextvars import Token
from typing import Generic
from pymicroservicesbase.sdk.sql.session.session_type import SessionType


class SessionContext(Generic[SessionType]):
    def __init__(self, database_session: SessionType) -> None:
        self.database_session = database_session
        self.token = None

    def get_token(self) -> Token:
        """
        Retrieve the token associated with this session context.
        This will be set once the context is registered.
        """
        if self.token is None:
            raise ValueError(
                "This context is not yet registered with a token."
            )
        return self.token

    def set_token(self, token: Token):
        self.token = token

    def get_session(self) -> SessionType:
        return self.database_session
