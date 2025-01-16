from __future__ import annotations
from datetime import datetime
from typing import Annotated, List, Literal, Sequence, Union

from fastapi import Depends
from pydantic import TypeAdapter, model_validator
import json

from .condition_param import ConditionParam

CompareOperatorType = Literal["eq", "neq", "gt", "lt", "gte", "lte"]
compare_operator_mapping: dict[CompareOperatorType, str] = {
    "eq": "=",
    "neq": "!=",
    "gt": ">",
    "lt": "<",
    "gte": ">=",
    "lte": "<=",
}

LogicGateOperatorType = Literal["and", "or", "not"]
# logic_gate_operator_mapping: Dict[LogicGateOperatorType, str] = {
#     "and": "&&",
#     "or": "||",
#     "not": "!",
# }

ListOperatorType = Literal["includes", "excludes"]
list_operator_mapping: dict[ListOperatorType, str] = {
    "includes": "in",
    "excludes": "not in",
}

OperatorType = Union[
    CompareOperatorType,
    # LogicGateOperatorType,
    ListOperatorType,
]
operator_mapping: dict[OperatorType | str, str] = {
    **compare_operator_mapping,
    # **logic_gate_operator_mapping,
    **list_operator_mapping,
}

FilterValueType = Union[int, str, datetime]


def get_operator_symbol(op: OperatorType | str) -> str:
    """Converts an operator name to its corresponding symbol."""
    try:
        return operator_mapping[op]
    except KeyError as e:
        raise Exception(f"invalid operator {op}") from e


class FilterParam(ConditionParam[FilterValueType, OperatorType]):
    @classmethod
    async def get_many_filters(
        cls, filters: str | None = None
    ) -> Sequence[FilterParam]:
        if filters is None:
            return []
        adapter = TypeAdapter(List[FilterParam])
        data = adapter.validate_python(json.loads(filters))
        return data

    @classmethod
    def get_filter(cls, filter: str | None = None) -> FilterParam | None:
        if filter is None:
            return None
        adapter = TypeAdapter(FilterParam)
        data = adapter.validate_python(json.loads(filter))
        return data

    @model_validator(mode="after")
    def validate_value(cls, filters):
        operator, value = (
            getattr(filters, "operator"),
            getattr(filters, "value"),
        )

        if operator in {"includes", "excludes"}:
            if isinstance(value, str):
                # Strings are valid for list operators
                pass
            elif isinstance(value, (int, datetime)):
                raise ValueError(
                    f"Operator '{operator}' is not valid for value type {type(value).__name__}. "
                    "List operators can only work with strings."
                )

        # elif operator in {"and", "or", "not"}:
        #     raise ValueError(
        #         f"Operator '{operator}' is invalid for individual values. "
        #         "Logic gate operators can only be used with combined conditions."
        #     )

        elif operator in {"eq", "neq", "gt", "lt", "gte", "lte"}:
            if isinstance(value, str):
                if operator in {"gt", "lt", "gte", "lte"}:
                    raise ValueError(
                        f"Operator '{operator}' is not valid for string values."
                        " Only 'eq' and 'neq' are allowed for strings."
                    )
            elif isinstance(value, int):
                # Integers are valid for all compare operators
                pass
            elif isinstance(value, datetime):
                # Datetimes are valid for all compare operators
                pass
            else:
                raise ValueError(
                    f"Unsupported value type: {type(value).__name__}."
                )

        # else:
        #     raise ValueError("Invalid operator for non-numeric value")

        # filters["operator"] = get_operator_symbol(operator)
        # setattr(filters,"operator",get_operator_symbol(operator))
        return filters


FilterParamsDep = Annotated[
    List[FilterParam], Depends(FilterParam.get_many_filters)
]
FilterParamDep = Annotated[FilterParam, Depends(FilterParam.get_filter)]
