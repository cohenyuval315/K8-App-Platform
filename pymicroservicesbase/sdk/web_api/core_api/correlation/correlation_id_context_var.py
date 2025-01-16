import contextvars

CorrelationIdContextVar = contextvars.ContextVar[str | None](
    "CorrelationIdContextVar", default=None
)
