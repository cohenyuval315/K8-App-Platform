from __future__ import annotations

import asyncio
import warnings
from types import TracebackType


class Timeout:
    def __init__(
        self,
        timeout: float | None,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
    ) -> None:
        self._timeout = timeout
        if loop is None:
            loop = asyncio.get_running_loop()
        else:
            warnings.warn(
                """The loop argument to timeout() is deprecated.""",
                DeprecationWarning,
            )
        self._loop = loop
        self._task = None
        self._cancelled = False
        self._cancel_handler = None
        self._cancel_at = None

    def __enter__(self) -> Timeout:
        return self._do_enter()

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> bool | None:
        self._do_exit(exc_type)
        return None

    async def __aenter__(self) -> Timeout:
        return self._do_enter()

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        self._do_exit(exc_type)

    @property
    def expired(self) -> bool:
        return self._cancelled

    @property
    def remaining(self) -> float | None:
        if self._cancel_at is not None:
            return max(self._cancel_at - self._loop.time(), 0.0)
        else:
            return None

    def _do_enter(self) -> Timeout:
        if self._timeout is None:
            return self

        self._task = asyncio.current_task(self._loop)
        if self._task is None:
            raise RuntimeError(
                "Timeout context manager should be used inside a task"
            )

        if self._timeout <= 0:
            self._loop.call_soon(self._cancel_task)
            return self

        self._cancel_at = self._loop.time() + self._timeout
        self._cancel_handler = self._loop.call_at(
            self._cancel_at, self._cancel_task
        )
        return self

    def _do_exit(self, exc_type: type[BaseException]) -> None:
        if exc_type is asyncio.CancelledError and self._cancelled:
            self._cancel_handler = None
            self._task = None
            raise asyncio.TimeoutError
        if self._timeout is not None and self._cancel_handler is not None:
            self._cancel_handler.cancel()
            self._cancel_handler = None
        self._task = None
        return None

    def _cancel_task(self) -> None:
        if self._task is not None:
            self._task.cancel()
            self._cancelled = True
