from typing import TypeVar
from abc import ABC, abstractmethod

from app.core.domain.aggregates import DomainAggregate
from app.core.domain.values import ID


Filter = TypeVar('Filter')


class IRepository[T: DomainAggregate](ABC):

    @abstractmethod
    def add(self, entity: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def remove_by_id(self, entity_id: ID) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, entity_id: ID) -> T:
        raise NotImplementedError

    def get_list(self, list_filter: Filter) -> list[T]:
        raise NotImplementedError

    def persist(self, entity: T) -> T:
        raise NotImplementedError
