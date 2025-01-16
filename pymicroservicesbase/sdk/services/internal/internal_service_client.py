from contextlib import asynccontextmanager
from http.cookiejar import CookieJar
from typing import (
    IO,
    Any,
    AsyncIterable,
    Callable,
    Dict,
    Iterable,
    List,
    Literal,
    Mapping,
    Sequence,
    Tuple,
)

import httpx

from pymicroservicesbase.shared.constants.headers import (
    CONTENT_LENGTH_HEADER_KEY,
)
from pymicroservicesbase.utils.patterns.singleton import SingletonMeta


class InternalServiceClient(metaclass=SingletonMeta):
    def __init__(
        self,
        host: str,
        port: int,
        prefix: str = "",
        protocol: Literal["http", "https"] = "http",
        headers: httpx.Headers | None = None,
        cookies: httpx.Cookies | None = None,
        timeout: httpx.Timeout = httpx.Timeout(timeout=5.0),
        limits: httpx.Limits = httpx.Limits(
            max_connections=100, max_keepalive_connections=20
        ),
        event_hooks: Mapping[str, List[Callable[..., Any]]] | None = None,
        *args: Any,
        **kwargs: Any,
    ):
        self.prefix = prefix
        self.timeout = timeout
        self.limits = limits
        self.host = host
        self.port = port
        self.base_url = f"{protocol}://{self.host}:{self.port}"
        self.max_redirects = 20
        self.trust_env = True

        self.http1 = True
        self.http2 = True
        self.follow_redirects = True
        self.default_encoding = "utf-8"
        self.event_hooks = event_hooks

        # self.max_content_length = 10000000
        # self.max_retries = 3
        # self.max_retry_length = 20
        # self.retry_on_timeout = False
        # self.stream_threshold = 100000
        self.headers = headers
        self.cookies = cookies

        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            default_encoding=self.default_encoding,
            follow_redirects=self.follow_redirects,
            limits=self.limits,
            timeout=self.timeout,
            cookies=self.cookies,
            http1=self.http1,
            http2=self.http2,
            max_redirects=self.max_redirects,
            trust_env=self.trust_env,
            event_hooks=self.event_hooks,
            *args,
            **kwargs,
        )

    def configure(self, **kwargs):
        for key, value in kwargs:
            if getattr(self, key) is not None:
                setattr(self, key, value)
        return self

    def with_headers(self, headers: List[Tuple[str, str]], **kwargs):
        merged_headers = []
        existing_headers = self.client.headers.multi_items()
        merged_headers.extend(existing_headers)
        merged_headers.extend(headers)
        self.client.headers = merged_headers
        self.headers = httpx.Headers(merged_headers)
        return self

    def with_purged_headers(
        self,
        headers: List[Tuple[str, str]],
        purge_headers: List[str],
        **kwargs,
    ):
        merged_headers = []
        existing_headers = self.client.headers.multi_items()
        merged_headers.extend(existing_headers)

        purged_headers = []
        for header, value in headers:
            if header not in purge_headers:
                purged_headers.append((header, value))

        merged_headers.extend(purged_headers)
        self.client.headers = merged_headers
        self.headers = httpx.Headers(merged_headers)
        return self

    def without_headers(self, headers: List[str], **kwargs):
        for header in headers:
            self.client.headers.pop(header, None)
            if self.headers is not None:
                self.headers.pop(header, None)
        return self

    def with_cookies(self, cookies: Dict[str, str], **kwargs):
        self.client.cookies = cookies
        return self

    @property
    def client(self) -> httpx.AsyncClient:
        """
        Getter for client
        """
        return self._client

    @client.setter
    def client(self, value: httpx.AsyncClient):
        """
        Setter for client
        """
        self._client = value

    async def close(self):
        await self.client.aclose()

    @asynccontextmanager
    async def with_client(self):
        async with self.client as c:
            yield c

    async def __aenter__(self):
        return self.client

    async def __aexit__(self, ext_type, exc_value, traceback):
        if not self.client.is_closed:
            await self.client.aclose()

    def trace(self, event_name, info):
        pass

    async def _request(
        self,
        method: str,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
    ):
        request = self._client.build_request(
            method=method,
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            # extensions={
            #     "trace": self.trace,
            # },
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return request

    async def _send(
        self, request: httpx.Request, stream: bool = False
    ) -> httpx.Response:
        r = await self.client.send(
            request=request,
            follow_redirects=True,
            stream=stream,
        )
        return r

    async def get(
        self,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
        stream: bool = False,
    ) -> httpx.Response:
        request = await self._request(
            method="GET",
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return await self._send(
            request=request,
            stream=stream,
        )

    async def post(
        self,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
        stream: bool = False,
    ) -> httpx.Response:
        request = await self._request(
            method="POST",
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return await self._send(
            request=request,
            stream=stream,
        )

    async def patch(
        self,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
        stream: bool = False,
    ) -> httpx.Response:
        request = await self._request(
            method="PATCH",
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return await self._send(
            request=request,
            stream=stream,
        )

    async def put(
        self,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
        stream: bool = False,
    ) -> httpx.Response:
        request = await self._request(
            method="PUT",
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return await self._send(
            request=request,
            stream=stream,
        )

    async def delete(
        self,
        url: httpx.URL | str,
        params: (
            Mapping[str, str]
            | Mapping[
                str,
                str
                | int
                | float
                | bool
                | Sequence[str | int | float | bool | None]
                | None,
            ]
            | List[Tuple[str, str | int | float | bool | None]]
            | Tuple[Tuple[str, str | int | float | bool | None], ...]
            | str
            | bytes
            | None
        ) = None,
        headers: httpx.Headers | None = None,
        cookies: (
            CookieJar | Dict[str, str] | List[Tuple[str, str]] | None
        ) = None,
        json: dict | None = None,
        data: Mapping[str, Any] | None = None,
        content: (
            str | bytes | Iterable[bytes] | AsyncIterable[bytes] | None
        ) = None,
        files: (
            Mapping[
                str,
                IO[bytes]
                | bytes
                | str
                | Tuple[str | None, IO[bytes] | bytes | str]
                | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                | Tuple[
                    str | None,
                    IO[bytes] | bytes | str,
                    str | None,
                    Mapping[str, str],
                ],
            ]
            | Sequence[
                Tuple[
                    str,
                    IO[bytes]
                    | bytes
                    | str
                    | Tuple[str | None, IO[bytes] | bytes | str]
                    | Tuple[str | None, IO[bytes] | bytes | str, str | None]
                    | Tuple[
                        str | None,
                        IO[bytes] | bytes | str,
                        str | None,
                        Mapping[str, str],
                    ],
                ]
            ]
            | None
        ) = None,
        timeout: httpx.Timeout | None = None,
        stream: bool = False,
    ) -> httpx.Response:
        request = await self._request(
            method="DELETE",
            url=url,
            json=json,
            data=data,
            content=content,
            files=files,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=timeout,
        )
        return await self._send(
            request=request,
            stream=stream,
        )

    async def get_request_body_length(self, request: httpx.Request):
        if request.method.strip().upper() in ["POST", "PUT", "PATCH"]:
            body_length = int(request.headers.get(CONTENT_LENGTH_HEADER_KEY))
            return body_length
        return 0

    async def get_response_body_length(self, response: httpx.Response):
        body_length = int(response.headers.get(CONTENT_LENGTH_HEADER_KEY))
        return body_length

    # async def handle_response(self, response: httpx.Response):
    #     content_length = response.headers.get(CONTENT_LENGTH_HEADER_KEY,None)
    #     transfer_encoding = response.headers.get(TRANSFER_ENCODING_HEADER_KEY, None)
    #     if content_length is not None:
    #         if transfer_encoding is not None:
    #             logger.warning(f"{content_length} {transfer_encoding}")

    #         content_length = int(content_length)
    #         if content_length < self.max_content_length:
    #             yield response.read()

    #     async for chunk in response.aiter_raw():
    #         yield chunk

    #     await response.aclose()

    # async def handle_retry(self, response: httpx.Response, retries: int, timeout: float):
    #     """Handle retries if Retry-After header is present."""
    #     retry_after:str | None = response.headers.get(RETRY_AFTER_HEADER_KEY, None)

    #     if retry_after is not None:
    #         # if retry_after.isdigit():
    #         #     retry_after_seconds = int(retry_after)
    #         try:
    #             retry_after_seconds = int(retry_after)
    #         except ValueError:
    #             # If Retry-After is a date string (e.g., RFC 7231 date format)
    #             import datetime
    #             from email.utils import parsedate_to_datetime
    #             retry_after_datetime = parsedate_to_datetime(retry_after)
    #             retry_after_seconds = (retry_after_datetime - datetime.datetime.utcnow()).total_seconds()
    #             retry_after_seconds = max(0, int(retry_after_seconds))  # Ensure we return a positive value

    #         if self.max_retry_length < retry_after_seconds:
    #             return 0

    #         logger.warning(f"Retrying after {retry_after_seconds} seconds. Retry {retries}/{self.max_retries}.")
    #         await asyncio.sleep(retry_after_seconds)
    #         return True

    #     return False
    #             retry_after_seconds = int(retry_after)
    #         except ValueError:
    #             # If Retry-After is a date string (e.g., RFC 7231 date format)
    #             import datetime
    #             from email.utils import parsedate_to_datetime
    #             retry_after_datetime = parsedate_to_datetime(retry_after)
    #             retry_after_seconds = (retry_after_datetime - datetime.datetime.utcnow()).total_seconds()
    #             retry_after_seconds = max(0, int(retry_after_seconds))  # Ensure we return a positive value

    #         if self.max_retry_length < retry_after_seconds:
    #             return 0

    #         logger.warning(f"Retrying after {retry_after_seconds} seconds. Retry {retries}/{self.max_retries}.")
    #         await asyncio.sleep(retry_after_seconds)
    #         return True

    #     return False
