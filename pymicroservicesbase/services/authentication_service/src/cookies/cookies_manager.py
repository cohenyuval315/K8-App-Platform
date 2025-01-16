from datetime import datetime
from typing import Dict, Literal

from fastapi import Request, Response


class CookiesManager:
    def __init__(
        self,
        path="/",
        domain: str | None = None,
        samesite: Literal["lax", "strict", "none"] | None = None,
        secure: bool = True,
        httponly: bool = True,
    ):
        self.path = path
        self.domain = domain
        self.secure = secure
        self.samesite: Literal["lax", "strict", "none"] | None = samesite
        self.httponly = httponly

    def set_cookie(
        self,
        response: Response,
        key: str,
        value: str,
        expire: datetime | str | int,
    ):
        # response.headers.append("set-cookie",
        response.set_cookie(
            key=key,
            value=value,
            expires=expire,
            path=self.path,
            domain=self.domain,
            httponly=self.httponly,
            samesite=self.samesite,
            secure=self.secure,
        )

    def get_cookies(self, request: Request) -> Dict[str, str]:
        return request.cookies

    def get_cookie(
        self, request: Request, key: str, default=None
    ) -> str | None:
        return request.cookies.get(key, default)

    def delete_cookie(
        self,
        response: Response,
        key: str,
    ):
        response.delete_cookie(
            key=key,
            path=self.path,
            domain=self.domain,
            httponly=self.httponly,
            samesite=self.samesite,
            secure=self.secure,
        )
