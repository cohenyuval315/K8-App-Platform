from typing import Literal


UvicornLoggerType = Literal[
    "uvicorn",
    "uvicorn.access",
    "uvicorn.error",
    "uvicorn.asgi",
]
