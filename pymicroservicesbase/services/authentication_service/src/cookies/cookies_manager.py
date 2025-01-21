from datetime import datetime, timedelta
from typing import Dict, Literal

from fastapi import Request, Response

from pymicroservicesbase.shared.constants.headers import SET_COOKIE_HEADER_KEY
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.utils.patterns.singleton import SingletonMeta


class CookiesManager(metaclass=SingletonMeta):
    def __init__(
        self,
        path="/",
        domain: str | None = None,
        samesite: Literal["lax", "strict", "none"] | None = None,
        secure: bool = True,
        httponly: bool = True,
        in_headers: bool = False,
        in_body: bool = False,
    ):
        self.configure(
            path, domain, samesite, secure, httponly, in_headers, in_body
        )

    def configure(
        self,
        path="/",
        domain: str | None = None,
        samesite: Literal["lax", "strict", "none"] | None = None,
        secure: bool = True,
        httponly: bool = True,
        in_headers: bool = False,
        in_body: bool = False,
    ):
        self.path = path
        self.domain = domain
        self.secure = secure
        self.samesite: Literal["lax", "strict", "none"] | None = samesite
        self.httponly = httponly
        self.in_headers = in_headers
        self.in_body = in_body
        return self

    def set_cookie(
        self,
        response: Response,
        key: str,
        value: str,
        expire: datetime | str | int,
        path: str | None = None,
        domain: str | None = None,
        samesite: Literal["lax", "strict", "none"] | None = None,
        secure: bool | None = None,
        httponly: bool | None = None,
    ):
        response.set_cookie(
            key=key,
            value=value,
            expires=expire,
            path=path or self.path,
            domain=domain or self.domain,
            httponly=httponly or self.httponly,
            samesite=samesite or self.samesite,
            secure=secure or self.secure,
        )

    def get_cookie_header(
        self,
        key: str,
        value: str,
        expire: datetime | str | int,
        path: str | None = None,
        domain: str | None = None,
        samesite: Literal["lax", "strict", "none"] | None = None,
        secure: bool | None = None,
        httponly: bool | None = None,
    ):
        cookie_header = f"{key}={value};"
        expires = self.format_expire(expire)
        if expires:
            cookie_header += f" Expires={expires};"
        if path:
            cookie_header += f" Path={path};"
        if domain:
            cookie_header += f" Domain={domain};"
        if httponly:
            cookie_header += " HttpOnly;"
        if samesite:
            cookie_header += f" SameSite={samesite};"
        if secure:
            cookie_header += " Secure;"
        header = (SET_COOKIE_HEADER_KEY, cookie_header)
        return header

    def format_expire(self, expire: datetime | str | int):
        if isinstance(expire, datetime):
            return expire.strftime("%a, %d %b %Y %H:%M:%S GMT")
        elif isinstance(expire, str):
            return expire
        elif isinstance(expire, int):
            expire_datetime = utcnow() + timedelta(seconds=expire)
            return expire_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")

    def get_cookies(self, request: Request) -> Dict[str, str]:
        return request.cookies

    def get_cookie(
        self, request: Request, key: str, default=None
    ) -> str | None:
        return request.cookies.get(key, default)

    def delete_cookie(self, response: Response, key: str):

        response.delete_cookie(
            key=key,
            path=self.path,
            domain=self.domain,
            httponly=self.httponly,
            samesite=self.samesite,
            secure=self.secure,
        )

    def delete_cookie_if_exists(
        self, response: Response, request: Request, key: str
    ):
        cookie = self.get_cookie(request, key)
        if cookie is not None:
            response.delete_cookie(
                key=key,
                path=self.path,
                domain=self.domain,
                httponly=self.httponly,
                samesite=self.samesite,
                secure=self.secure,
            )
