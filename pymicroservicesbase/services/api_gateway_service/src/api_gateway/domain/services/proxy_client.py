from ssl import SSLContext
from typing import Any, Callable, List, Mapping
from fastapi import Request
import httpx
from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.shared.constants.headers import (
    CONTENT_LENGTH_HEADER_KEY,
    HOST_HEADER_KEY,
)
from pymicroservicesbase.utils.patterns.singleton import SingletonMeta
from pymicroservicesbase.services.api_gateway_service.logger import logger


class ProxyClient(metaclass=SingletonMeta):
    def __init__(
        self,
        headers: httpx.Headers | None = None,
        cookies: httpx.Cookies | None = None,
        timeout: httpx.Timeout = httpx.Timeout(timeout=5.0),
        limits: httpx.Limits = httpx.Limits(
            max_connections=100, max_keepalive_connections=20
        ),
        chunk_size: int | None = None,
        event_hooks: Mapping[str, List[Callable[..., Any]]] | None = None,
        cert=None,
        verify: SSLContext | str | bool = False,
        proxy=None,
        mounts=None,
        *args: Any,
        **kwargs: Any,
    ):
        self.timeout = timeout
        self.limits = limits
        self.max_redirects = 20
        self.trust_env = True
        self.chunk_size = chunk_size

        self.http1 = True
        self.http2 = True
        self.follow_redirects = True
        self.default_encoding = "utf-8"
        self.event_hooks = event_hooks
        self.headers = headers
        self.cookies = cookies
        self.verify = verify
        self.proxy = proxy
        self.mounts = mounts
        self.cert = cert

        self._client = httpx.AsyncClient(
            cert=self.cert,
            mounts=self.mounts,
            proxy=self.proxy,
            verify=self.verify,
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

    @property
    def client(self) -> httpx.AsyncClient:
        """
        Getter for client
        """
        return self._client

    @client.setter
    def client(self, client) -> None:
        """
        Setter for client
        """
        self._client = client

    async def close(self):
        if not self.client.is_closed:
            await self._client.aclose()

    async def forward_request(
        self,
        method: str,
        url: httpx.URL | str,
        request: Request,
        *,
        timeout: httpx.Timeout | None = None,
    ):
        headers = httpx.Headers(request.headers)
        headers.pop(CONTENT_LENGTH_HEADER_KEY, None)
        headers.pop(HOST_HEADER_KEY, None)

        _request = self.client.build_request(
            method=method,
            url=url,
            params=request.query_params,
            headers=headers,
            cookies=request.cookies,
            timeout=timeout,
            content=await request.body(),
        )
        _response = await self.client.send(
            _request,
            # stream=True
        )
        return _response

    async def forward_request_stream(
        self,
        method: str,
        url: httpx.URL | str,
        request: Request,
        *,
        timeout: httpx.Timeout | None = None,
    ):
        async with self.client.stream(
            method=method,
            url=url,
            headers=request.headers.raw,
            cookies=request.cookies,
            params=request.query_params,
            content=request.stream(),
            timeout=timeout,
        ) as forwarded_response:
            if forwarded_response.is_error:
                if forwarded_response.is_server_error:
                    logger.error("server error")
                    return
                if forwarded_response.is_client_error:
                    logger.error("client error")
                    pass

                raise WebServiceError(
                    error_code=forwarded_response.status_code,
                    error_message="api gateway recv error response",
                    is_public=False,
                    include_trace_errors=True,
                    errors=[forwarded_response.json()],
                )
                return

            async for chunk in forwarded_response.aiter_bytes(self.chunk_size):
                if await request.is_disconnected():
                    await self.on_disconnect(request)
                    break
                yield chunk

    async def on_disconnect(self, request: Request):
        logger.warning("disconnect...")
