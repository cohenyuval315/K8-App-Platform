from io import BytesIO
import time
from starlette.datastructures import MutableHeaders, Headers
from starlette.types import ASGIApp, Scope, Receive, Send, Message
from pymicroservicesbase.sdk.web_api.core_api.logging.web_service_logger import (
    WebServiceLogger,
)
import logging
import aiofiles

# async def get_response(scope, receive, send) -> Response:
#     """
#     Fetch the response content.
#     Here we're accessing the `response` as a streaming object.
#     """
#     response = await receive()
#             # if isinstance(response, StreamingResponse):
#             #     return await process_streaming_response(self.logger, response)
#             # elif isinstance(response, Response):
#             #     return await process_regular_response(self.logger, response)


#     return response

# async def process_streaming_response(logger, response: StreamingResponse):
#     """
#     Process a StreamingResponse by reading its chunks.
#     """
#     async def stream_with_reading():
#         async for chunk in response.body_iterator:
#             logger.debug(chunk)
#             yield chunk

#     return StreamingResponse(stream_with_reading(), media_type=response.media_type)


# async def receive_logging_request_body_size():
#     body_size = 0
#     nonlocal body_size

#     message = await receive()
#     assert message["type"] == "http.request"

#         print(f"Size of request body was: {body_size} bytes")

#     return message


# async def process_regular_response(logger, response: Response):
#     """
#     Process a regular response by reading and handling the content asynchronously.
#     """
#     body = await response.body() # type: ignore
#     logger.debug(body)
#     return Response(content=body, status_code=response.status_code, headers=response.headers, media_type=response.media_type)


class LoggingMiddleware:
    def __init__(
        self, app: ASGIApp, logger: WebServiceLogger | logging.Logger
    ) -> None:
        self.app = app
        self.logger = logger
        self.request_body_buffer = BytesIO()
        self.response_body_buffer = BytesIO()
        self.request_headers = None
        self.response_headers = None

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        async with (
            aiofiles.tempfile.NamedTemporaryFile(
                mode="w+b"
            ) as request_body_file,
            aiofiles.tempfile.NamedTemporaryFile(
                mode="w+b"
            ) as response_body_file,
        ):
            start_time = time.perf_counter()

            async def inner_receive():
                message = await receive()
                if message["type"] == "http.request":
                    self.request_headers = Headers(scope=scope)
                    body = message.get("body", b"")
                    more_body = not message.get("more_body", False)
                    await request_body_file.write(body)
                    if not more_body:
                        await request_body_file.seek(0)
                return message

            async def inner_send(message: Message) -> None:
                # recv_obj = json.dumps(message,indent=2)
                message_type = message["type"]

                if message_type == "http.response.start":
                    # self.logger.debug(f"Response Headers: {headers}\n\n")
                    # response_headers = Headers(message)
                    self.response_headers = MutableHeaders(scope=message)

                if message_type == "http.response.body":
                    body = message.get("body", b"")
                    more_body = message.get("more_body", False)
                    await response_body_file.write(body)
                    if not more_body:
                        await response_body_file.seek(0)
                        process_time = time.perf_counter() - start_time

                        request_body = await self._read_payload(
                            request_body_file
                        )
                        response_body = await self._read_payload(
                            response_body_file
                        )

                        log_details = {
                            "request_headers": (
                                self.request_headers.raw
                                if self.request_headers
                                else None
                            ),
                            "request_body": request_body,
                            "response_headers": (
                                self.response_headers.raw
                                if self.response_headers
                                else None
                            ),
                            "response_body": response_body,
                            "process_time": process_time,
                        }
                        self.log_request_response(log_details)
                        # BackgroundTask(self.log_request_response, log_details)

                await send(message)

            await self.app(scope, inner_receive, inner_send)

        return

    async def _read_payload(self, file) -> str:
        """Read payload from a file, efficiently handling large data."""
        await file.seek(0)
        return (await file.read()).decode("utf-8", errors="replace")

    def log_request_response(self, details: dict) -> None:
        self.logger.info(
            "Request and Response Log:\n"
            f"Request Headers: {details['request_headers']}\n"
            f"Request Body: {details['request_body']}\n"
            f"Response Headers: {details['response_headers']}\n"
            f"Response Body: {details['response_body']}\n"
            f"Processing Time: {details['process_time']:.4f} seconds\n"
        )
