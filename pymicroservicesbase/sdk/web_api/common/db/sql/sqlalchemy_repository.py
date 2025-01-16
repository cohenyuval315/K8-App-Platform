import operator
from typing import (
    Any,
    Dict,
    Generic,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
)

import sqlalchemy as sa
from sqlalchemy import Select, delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased
from sqlalchemy.sql import expression

from pymicroservicesbase.shared.logging import logger


SortOrderType = Literal["asc", "desc", "ASC", "DESC", 1, -1]

FILTERING_OPERATORS = {
    "in": "in_",
    "eq": operator.eq,
    "not": "__ne__",
    "gte": "__ge__",
    "lte": "__le__",
    "gt": "__gt__",
    "lt": "__lt__",
    "like": "like",
}

OPERATORS = {
    # Equality
    "eq": lambda x, y: x == y,
    "=": lambda x, y: x == y,
    "==": lambda x, y: x == y,
    # Inequality
    "ne": lambda x, y: x != y,
    "!=": lambda x, y: x != y,
    "<>": lambda x, y: x != y,  # SQL-style inequality
    # Less than
    "lt": lambda x, y: x < y,
    "<": lambda x, y: x < y,
    # Less than or equal
    "le": lambda x, y: x <= y,
    "<=": lambda x, y: x <= y,
    # Greater than
    "gt": lambda x, y: x > y,
    ">": lambda x, y: x > y,
    # Greater than or equal
    "ge": lambda x, y: x >= y,
    ">=": lambda x, y: x >= y,
    # Logical operators
    "and": lambda x, y: x and y,
    "&&": lambda x, y: x and y,
    "or": lambda x, y: x or y,
    "||": lambda x, y: x or y,
    "not": lambda x: not x,
    "!": lambda x: not x,
    # Arithmetic operators
    "add": lambda x, y: x + y,
    "+": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "-": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "*": lambda x, y: x * y,
    "div": lambda x, y: x / y,
    "/": lambda x, y: x / y,
    "mod": lambda x, y: x % y,
    "%": lambda x, y: x % y,
    "pow": lambda x, y: x**y,
    "**": lambda x, y: x**y,
    # Bitwise operators
    "bit_and": lambda x, y: x & y,
    "&": lambda x, y: x & y,
    "bit_or": lambda x, y: x | y,
    "|": lambda x, y: x | y,
    "bit_xor": lambda x, y: x ^ y,
    "^": lambda x, y: x ^ y,
    "bit_not": lambda x: ~x,
    "~": lambda x: ~x,
    "bit_shift_left": lambda x, y: x << y,
    "<<": lambda x, y: x << y,
    "bit_shift_right": lambda x, y: x >> y,
    ">>": lambda x, y: x >> y,
    # Membership and identity
    "in": lambda x, y: x in y,
    "not_in": lambda x, y: x not in y,
    "is": lambda x, y: x is y,
    "is_not": lambda x, y: x is not y,
    # SQL-like operators
    "like": lambda x, y: y in x,  # Simplified
    "ilike": lambda x, y: y.lower() in x.lower(),  # Simplified
    "between": lambda x, y: y[0] <= x <= y[1],
    "not_between": lambda x, y: not (y[0] <= x <= y[1]),
}


BaseModelType = TypeVar("BaseModelType", bound=Any)


class SQLAlchemyRepository(Generic[BaseModelType]):
    """Base class for data repositories."""

    def __init__(self, model_class, db_session: AsyncSession):
        self.model_class = model_class
        self._model_cls = model_class
        self.session = db_session
        logger.debug(
            f"Initialized repository for model: {model_class.__name__}"
        )

    def _select(self) -> Select:
        """Selects the model."""
        logger.debug(f"Selecting model: {self.model_class.__name__}")
        return select(self.model_class)

    async def create(
        self, attributes: Optional[dict[str, Any]] = None
    ) -> BaseModelType:
        """Create sqlalchemy model instance."""
        logger.debug(
            f"Creating instance of {self.model_class.__name__} with attributes: {attributes}"
        )
        if attributes is None:
            attributes = {}
        model = self.model_class(**attributes)
        self.session.add(model)
        await self.session.flush()
        logger.info(
            f"Created new {self.model_class.__name__} instance with ID: {model.id}"
        )
        return model

    async def create_many(
        self, models_attributes: List[dict[str, Any]] | None = None
    ) -> List[BaseModelType]:
        """Create many sqlalchemy model instances."""
        if models_attributes is None:
            models_attributes = []
        model_instances = []
        for attributes in models_attributes:
            model = self.model_class(**attributes)
            self.session.add(model)
            model_instances.append(model)
        await self.session.flush()
        logger.info(
            f"Created {len(model_instances)} new instances of {self.model_class.__name__}"
        )
        return model_instances

    async def flush(self):
        logger.debug("Flushing session.")
        await self.session.flush()
        return self

    async def _execute(self, stmt):
        logger.debug(f"Executing SQL statement: {stmt}")
        return await self.session.execute(stmt)

    async def update_by_id(
        self, model_id: str, attributes: Dict[str, Any], *args, **kwargs
    ):
        # Avoids read-modify-write anti-pattern race conditions
        logger.debug(
            f"Updating {self.model_class.__name__} with ID {model_id} using attributes: {attributes}"
        )
        stmt = (
            update(self._model_cls)
            .where(self._model_cls.id == model_id)
            .values(**attributes)
            .returning(self._model_cls)
            .execution_options(*args, **kwargs)
        )
        result = await self.session.execute(stmt)
        await self.session.flush()
        logger.info(f"Updated {self.model_class.__name__} with ID {model_id}")
        return result.scalar_one()

    async def delete_by_id(self, model_id: str, *args, **kwargs):
        logger.debug(
            f"Deleting {self.model_class.__name__} with ID {model_id}"
        )
        stmt = (
            delete(self._model_cls)
            .where(self._model_cls.id == model_id)
            .returning(self._model_cls)
            .execution_options(*args, **kwargs)
        )
        result = await self.session.execute(stmt)
        await self.session.flush()
        logger.info(f"Deleted {self.model_class.__name__} with ID {model_id}")
        return result.scalar_one()

    async def query(self, text: str) -> Any:
        logger.debug(f"Executing raw SQL query: {text}")
        result = await self.session.execute(sa.text(text))
        return result

    async def count(self, criteria: Select) -> int:
        """Count the sqlalchemy query."""
        logger.debug("Counting results for the criteria.")
        count_query = criteria.subquery()
        result = await self.session.scalars(
            statement=select(func.count()).select_from(count_query)
        )
        count = result.one()
        logger.info(f"Counted {count} results for the criteria.")
        return count

    async def fetch_all(self, criteria: Select) -> Sequence[BaseModelType]:
        """Fetch all and execute sqlalchemy query."""
        logger.debug(f"Fetching all results for the criteria: {criteria}")
        result = await self.session.scalars(criteria)
        return result.all()

    async def fetch_one(self, criteria: Select) -> Optional[BaseModelType]:
        """Fetch one and execute sqlalchemy query."""
        logger.debug(f"Fetching one result for the criteria: {criteria}")
        result = await self.session.scalars(criteria)
        return result.one_or_none()

    def apply_join(
        self, criteria: Select, join: Optional[Dict[str, Any]] = None
    ) -> Select:
        """Join the criteria."""
        if join is None:
            return criteria

        model = join.get("model", None)
        on_condition = join.get("on_condition", None)
        is_outer = join.get("is_outer", False)
        is_full = join.get("is_full", False)

        if on_condition is None or model is None:
            return criteria

        if not isinstance(model, Type):
            raise ValueError("invalid model. model must be a class")

        # origin = getattr(model, "__origin__", None)
        # if origin is not None and not issubclass(origin, BaseTable):
        #     raise ValueError("Invalid model type. model must be a subclass of Base.")

        if not isinstance(is_outer, bool):
            raise ValueError("is_outer must be boolean")

        if not isinstance(is_full, bool):
            raise ValueError("is_full must be boolean")

        if not isinstance(on_condition, expression.ColumnElement):
            raise ValueError("condition must be a clause element")

        criteria = criteria.join(
            aliased(model), on_condition, isouter=is_outer, full=is_full
        )
        logger.debug(f"Applied join with model: {model.__name__}")
        return criteria

    def apply_filter(self, criteria: Select, _filter) -> Select:
        """Adds a filter condition to the query by field and value."""
        if _filter is None:
            return criteria
        logger.info(f"Applying filter: {_filter}")
        filter_by = _filter["field"]
        value = _filter["value"]
        operator = _filter["operator"]
        operator_func = OPERATORS[operator]
        criteria = criteria.where(
            operator_func(getattr(self._model_cls, filter_by), value)
        )

        return criteria

    def apply_sort(self, criteria: Select, _sort) -> Select:
        """Sort the sqlalchemy query."""
        if _sort is None:
            return criteria
        sort_by = _sort["field"]
        sort_order = _sort["value"]

        if sort_by is None or sort_order is None:
            return criteria

        if not hasattr(self.model_class, sort_by):
            raise ValueError(
                f"Property '{sort_by}' does not exist on the model."
            )

        _sort_order = sort_order

        if isinstance(sort_order, str):
            _sort_order = sort_order.lower()

        elif isinstance(sort_order, int):
            if sort_order == 1:
                _sort_order = "asc"
            elif sort_order == -1:
                _sort_order = "desc"

        if _sort_order == "asc":
            criteria = criteria.order_by(
                getattr(self.model_class, sort_by).asc()
            )
        elif _sort_order == "desc":
            criteria = criteria.order_by(
                getattr(self.model_class, sort_by).desc()
            )
        else:
            raise ValueError(
                f"Invalid sort_order value: {sort_order}. Expected one of: {SortOrderType}"
            )
        logger.debug(f"Applied sort by {sort_by} in {sort_order} order.")
        return criteria

    def apply_pagination(
        self,
        criteria: Select,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Select:
        """Paginate the sqlalchemy query."""
        if offset is not None:
            if offset < 0:
                raise ValueError("offset cannot be lower than 0")
            criteria = criteria.offset(offset)
        if limit is not None:
            if limit < 0:
                raise ValueError("limit cannot be lower than 0")
            criteria = criteria.limit(limit)
        logger.debug(
            f"Applied pagination with offset: {offset}, limit: {limit}"
        )
        return criteria

    async def add_sort(
        self, query: Select, sort_by: str, order: str = "asc"
    ) -> Select:
        """Adds sorting to the query by the specified column and order."""
        order_column = getattr(self.model_class, sort_by)
        return query.order_by(
            order_column.desc() if order == "desc" else order_column.asc()
        )

    def apply_joins(
        self, criteria: Select, joins: Optional[List[Dict[str, Any]]] = None
    ) -> Select:
        """Joins the multiple tables."""
        if joins is not None:
            for join in joins:
                criteria = self.apply_join(criteria, join)
        return criteria

    def apply_filtering(
        self, criteria: Select, filters: Optional[List[Any]] = None
    ) -> Select:
        """Filter the criteria."""
        if filters is not None:
            for _filter in filters:
                criteria = self.apply_filter(criteria, _filter)
        return criteria

    def apply_sorting(
        self, criteria: Select, sorts: Optional[List[Any]] = None
    ) -> Select:
        """multiple sorting sqlalchemy query."""
        if sorts is not None:
            for _sort in sorts:
                self.apply_sort(criteria, _sort)
        return criteria

    def build_criteria(
        self,
        joins: Optional[List[Dict[str, Any]]] = None,
        filters: Optional[List[Any]] = None,
        sorts: Optional[List[Any]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Select:
        """Builds criteria for the model, applying joins and ordering if provided."""
        criteria = self._select()
        criteria = self.apply_joins(criteria, joins)
        criteria = self.apply_filtering(criteria, filters)
        criteria = self.apply_sorting(criteria, sorts)
        criteria = self.apply_pagination(criteria, offset, limit)
        logger.debug(f"Built criteria: {criteria}")
        return criteria

    async def get_all(self) -> Optional[Tuple[Sequence[BaseModelType], int]]:
        """Get all model instances."""
        return await self.get_many()

    async def get_many(
        self,
        joins: Optional[List[Dict[str, Any]]] = None,
        filters: Optional[List[Any]] = None,
        sorts: Optional[List[Any]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        *args,
        **kwargs,
    ) -> Tuple[Sequence[BaseModelType], int]:
        """Returns the model instances matching the configuration"""
        criteria = self.build_criteria(
            joins=joins,
            filters=filters,
            sorts=sorts,
            limit=limit,
            offset=offset,
        )

        count = await self.count(criteria)

        many = await self.fetch_all(criteria)
        logger.info(f"Fetched {len(many)} instances with count: {count}")
        return (many, count)

    async def get_one(
        self,
        joins: Optional[List[Dict[str, Any]]] = None,
        filters: Optional[List[Dict[str, Any]]] = None,
        *args,
        **kwargs,
    ) -> Optional[BaseModelType]:
        """Returns the model instance matching the field and value."""
        criteria = self.build_criteria(
            joins=joins,
            filters=filters,
        )
        one = await self.fetch_one(criteria)
        if one:
            logger.info(f"Fetched one {self.model_class.__name__} instance.")
        else:
            logger.warning(
                f"No {self.model_class.__name__} instance found for the criteria."
            )
        return one
