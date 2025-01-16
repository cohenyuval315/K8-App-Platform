from __future__ import annotations

from pydantic import (
    BaseModel as PydanticBaseModel,
    ConfigDict,
    PrivateAttr,
)
from datetime import datetime


class BaseModel(PydanticBaseModel):
    """
    Base pydantic model.
    """

    _defined_at: datetime = PrivateAttr(default_factory=datetime.now)

    # @field_serializer("_defined_at")
    # def serialize_timestamp(self, value: datetime) -> str:
    #     return value.isoformat()

    model_config = ConfigDict(
        # json_encoders={
        #     datetime: datetime_to_string
        # },
        populate_by_name=True,
        validation_error_cause=True,
        extra="allow",
        strict=False,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    # @classmethod
    # def model_parametrized_name(cls, params: Tuple[Type[Any], ...]) -> str:
    #     return f"{params[0].__name__.title()}Schema"

    def to_model(self, model: BaseModel) -> BaseModel:
        return self.model_validate(model)

    def model_dump(
        self,
        *,
        mode="python",
        include=None,
        exclude=None,
        context=None,
        by_alias=False,
        exclude_unset=False,
        exclude_defaults=False,
        exclude_none=True,  # set to True
        round_trip=False,
        warnings=True,
        serialize_as_any=False,
    ):
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            serialize_as_any=serialize_as_any,
        )

    def model_dump_json(
        self,
        *,
        indent=None,
        include=None,
        exclude=None,
        context=None,
        by_alias=False,
        exclude_unset=False,
        exclude_defaults=False,
        exclude_none=True,
        round_trip=False,
        warnings=True,
        serialize_as_any=False,
    ):
        return super().model_dump_json(
            indent=indent,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            serialize_as_any=serialize_as_any,
        )
