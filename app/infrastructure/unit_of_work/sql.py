import attrs

from app.core.unit_of_work import BaseUOW
from app.core.repository import IRepository
from app.domain.entities import ComplexMeal, DetailedMeal


@attrs.define
class SQLUnitOfWork(BaseUOW):
    repo: IRepository[ComplexMeal | DetailedMeal]
