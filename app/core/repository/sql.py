import attrs

from abc import ABC, abstractmethod
from typing import Any, Optional, cast

from sqlalchemy.sql.expression import select
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.orm.session import Session

from app.core.domain.aggregates import DomainAggregate
from app.core.models import ORMBase
from app.core.repository import IRepository
from app.core.schema import Filter


@attrs.define
class SQLRepositoryMixin(ABC):
    session: Session


class GenericSQLRepository[T: DomainAggregate, M:  ORMBase](SQLRepositoryMixin, IRepository[T]):
    model: Any

    def add(self, entity: T) -> T:
        entity_orm: M = self._entity_to_orm(entity)
        self.session.add(entity_orm)
        self.session.flush()
        return entity

    def get_by_name(self, entity_name: str) -> list[T]:
        stmt = select(self.model).filter(self.model.name == entity_name)
        orm_models = self.session.scalars(stmt).unique()
        if not orm_models:
            raise ValueError(f"Entity with name '{entity_name}' was not found")
        return self._entities_from_orm(list(orm_models))

    def get_list(self, list_filter: Optional[Filter] = None) -> list[T]:
        stmt = select(self.model)
        results: list[T] = []
        if list_filter is not None:
            if list_filter.filter is not None:
                for key, value in list_filter.filter.items():
                    model_column = getattr(self.model, key, None)
                    if model_column is None:
                        # TODO: Implement custom exception classes
                        raise ValueError(f"Entity cannot be filtered by attribute '{key}'")
                    if isinstance(value, (list, tuple)):
                        stmt += stmt.filter(cast(ColumnElement, model_column.in_(value)))
                    else:
                        stmt += stmt.filter(cast(ColumnElement, model_column == value))

            if list_filter.name is not None:
                for name in list_filter.name:
                    entities: list[T] = self.get_by_name(name)
                    results.extend(entities)
        return results

    def _entities_from_orm(self, entities: list[M]) -> list[T]:
        return list(map(self._entity_from_orm, entities))

    @abstractmethod
    def _entity_to_orm(self, entity: T) -> M:
        pass

    @abstractmethod
    def _entity_from_orm(self, entity_orm: M) -> T:
        pass
