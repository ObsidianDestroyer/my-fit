from abc import ABC, abstractmethod
from typing import TypeVar, Optional

from app.core.domain.aggregates import DomainAggregate
from app.core.domain.values import ID


Filter = TypeVar('Filter')


class IRepository[T: DomainAggregate](ABC):

    # NOTE: Temporary muted
    # @abstractmethod
    def add(self, entity: T) -> T:
        raise NotImplementedError

    # NOTE: Temporary muted
    # @abstractmethod
    def remove_by_id(self, entity_id: ID) -> None:
        raise NotImplementedError

    # NOTE: Temporary muted
    # @abstractmethod
    def get_by_id(self, entity_id: ID) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_list(self, list_filter: Optional[Filter] = None) -> list[T]:
        raise NotImplementedError

    # NOTE: Temporary muted
    # @abstractmethod
    def persist(self, entity: T) -> T:
        raise NotImplementedError
