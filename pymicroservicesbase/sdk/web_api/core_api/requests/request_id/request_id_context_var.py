import contextvars

RequestIdContextVar = contextvars.ContextVar[str | None](
    "RequestIdContextVar", default=None
)
