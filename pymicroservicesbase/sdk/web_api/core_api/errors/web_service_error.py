from __future__ import annotations
from typing import Any, TypedDict
from collections import deque
from pymicroservicesbase.shared.errors import BaseError


class ErrorDict(TypedDict):
    error_code: str | int
    message: str
    is_public: bool
    include_trace_errors: bool
    errors: list[Any]


class WebServiceError(BaseError):
    ERROR = "error"
    ERROR_CODE = "error_code"
    ERROR_MSG = "message"
    IS_PUBLIC = "is_public"
    INC_TRACE = "include_trace_errors"
    ERRORS = "errors"
    SOURCE = "source"

    def __init__(
        self,
        *args: Any,
        error_code: int | str | None = None,
        error_message: str | None = None,
        is_public: bool = False,
        include_trace_errors: bool = True,
        errors: list[Any] | None = None,
        **kwargs: Any,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.is_public = is_public
        self.include_trace_errors = include_trace_errors
        self.errors = errors

    @classmethod
    def to_dict(cls, error: dict) -> dict[str, Any]:
        """
        Converts the current error into a dictionary.
        """
        return {
            cls.ERROR_CODE: error.get(cls.ERROR_CODE),
            cls.ERROR_MSG: error.get(cls.ERROR_MSG),
            cls.IS_PUBLIC: error.get(cls.IS_PUBLIC, False),
            cls.INC_TRACE: error.get(cls.INC_TRACE, True),
            cls.ERRORS: error.get(cls.ERRORS, []),
        }

    @classmethod
    def to_public(cls, error: dict) -> dict[str, Any]:
        """
        Converts the current error into a dictionary.
        """
        return {
            cls.ERROR: error.get(cls.ERROR_MSG),
            cls.ERROR_MSG: error.get(cls.ERROR_MSG),
        }

    def as_dict(self) -> dict[str, Any]:
        """
        Converts the current error into a dictionary.
        """

        d = {
            self.ERROR_CODE: self.error_code,
            self.ERROR_MSG: self.error_message,
            self.IS_PUBLIC: self.is_public,
            self.INC_TRACE: self.include_trace_errors,
            self.ERRORS: self.errors,
        }

        return d

    def flatten_public_dict_dfs(self):
        result = []

        def traverse(node):
            err = self.to_dict(node)
            errors = err.pop(self.ERRORS, [])

            if err.get(self.IS_PUBLIC) is True:
                result.append(self.to_public(err))

            if err.get(self.INC_TRACE) is True:
                for child in errors:
                    traverse(child)

        traverse(self.as_dict())
        return result

    @classmethod
    def flatten_errors(cls, errors):
        result = []

        def traverse(node):
            err = cls.to_dict(node)
            errors = err.pop(cls.ERRORS, [])

            if err.get(cls.IS_PUBLIC) is True:
                result.append(cls.to_public(err))

            if err.get(cls.INC_TRACE) is True:
                for child in errors:
                    traverse(child)

        traverse(errors)
        return result

    def flatten_public_dict_bfs(self):
        result = []
        queue = deque([self.as_dict()])
        while queue:
            current = queue.popleft()
            err = self.to_dict(current)
            errors = err.pop(self.ERRORS, [])
            if err.get(self.IS_PUBLIC) is True:
                result.append(self.to_public(err))

            if err.get(self.INC_TRACE) is True:
                for child in errors:
                    queue.append(child)
        return result

    @classmethod
    def flatten(cls, errors: list[Any]):
        result = []
        queue = deque([err for err in errors])
        while queue:
            current = queue.popleft()

            err = cls.to_dict(current)
            errors = err.pop(cls.ERRORS, [])
            if err.get(cls.IS_PUBLIC, False) is True:
                result.append(cls.to_public(err))

            if err.get(cls.INC_TRACE, True) is True and errors is not None:
                for child in errors:
                    queue.append(child)
        return result

    @classmethod
    def to_public_dict(cls, error: dict):
        return {
            cls.ERROR: error.get(cls.ERROR_CODE),
            cls.ERROR_MSG: error.get(cls.ERROR_MSG),
        }

    @classmethod
    def pack(cls, errors: list[Any]) -> dict[str, Any]:
        """
        Packs a list of errors into the `{errors: [...]}` structure.
        """
        return {"errors": errors}

    @classmethod
    def unpack(cls, response: dict[str, Any]) -> list[Any]:
        """
        Unpacks the `{errors: [...]}` structure into a list of errors.
        """
        return response.get("errors", [])


if __name__ == "__main__":
    import json

    def pprint(o, k="value"):
        f"--------{k}------------\n"
        print(json.dumps(o, indent=2))
        f"--------{k}------------\n"

    error = WebServiceError(
        error_code=123,
        error_message="A critical error occurred.",
        is_public=True,
        include_trace_errors=True,
        errors=[
            {
                "error_code": 789,
                "message": "Sub-error from another service",
                "is_public": True,
                "include_trace_errors": True,
                "errors": [
                    {
                        "error_code": 1011,
                        "message": "Sub-error from another service",
                        "is_public": True,
                        "include_trace_errors": True,
                        "errors": [
                            {
                                "error_code": 1213,
                                "message": "Sub-error from another service",
                                "is_public": True,
                                "include_trace_errors": True,
                                "errors": [],
                            },
                            {
                                "error_code": 1415,
                                "message": "Sub-error from another service",
                                "is_public": True,
                                "include_trace_errors": True,
                                "errors": [
                                    {
                                        "error_code": 1617,
                                        "message": "Sub-error from another service",
                                        "is_public": True,
                                        "include_trace_errors": True,
                                        "errors": [],
                                    }
                                ],
                            },
                            {
                                "error_code": 1819,
                                "message": "Sub-error from another service",
                                "is_public": False,
                                "include_trace_errors": True,
                                "errors": [
                                    {
                                        "error_code": 2021,
                                        "message": "Sub-error from another service",
                                        "is_public": True,
                                        "include_trace_errors": True,
                                        "errors": [],
                                    }
                                ],
                            },
                        ],
                    },
                ],
            },
            {
                "error_code": 2223,
                "message": "Sub-error from another service",
                "is_public": True,
                "include_trace_errors": False,
                "errors": [],
            },
        ],
    )

    # To get the public error structure (error and message only):
    print("Public Error Structure:")
    pprint(error.flatten_public_dict_bfs())

    # # To get all errors (without flattening, keeping the hierarchy):
    # print("\nFull Error Structure (Nested):")
    # pprint(error.get_all_errors(flatten=False))

    # # To get all errors (flattened list of errors):
    # print("\nFull Error Structure (Flattened):")
    # pprint(error.get_all_errors(flatten=True))
    # print("\nFull Error Structure (Flattened):")
    # pprint(error.get_all_errors(flatten=True))
