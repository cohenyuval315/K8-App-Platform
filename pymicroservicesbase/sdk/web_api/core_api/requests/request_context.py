from fastapi import Request
import uuid
from contextvars import Token


class RequestContext:
    def __init__(self, request: Request):
        self._request = request
        self._token = None
        self._id = self.generate_request_id()

    def set_token(self, token: Token):
        self._token = token

    def get_token(self) -> Token | None:
        return self._token

    def get_request(self) -> Request:
        return self._request

    def generate_request_id(self) -> str:
        request_id = str(uuid.uuid4())
        prefix = "request"
        request_string = prefix + request_id
        return request_string
