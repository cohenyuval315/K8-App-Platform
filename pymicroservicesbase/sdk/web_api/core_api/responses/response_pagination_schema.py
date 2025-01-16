from typing_extensions import TypedDict


class ResponsePaginationSchema(TypedDict):
    """Pagination Schema
    pagination data
    """

    total: int
    page_size: int
    page: int
