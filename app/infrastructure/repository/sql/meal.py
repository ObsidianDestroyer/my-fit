import contextlib

from typing import TypeAlias, Never

from pydantic import ValidationError

from app.core.repository.sql import GenericSQLRepository

from app.domain.entities import ComplexMeal, DetailedMeal
from app.infrastructure.models import MealORM


MixinMeal: TypeAlias = ComplexMeal | DetailedMeal


class SQLMealRepository(GenericSQLRepository[MixinMeal, MealORM]):
    model = MealORM

    def _entity_from_orm(self, entity_orm: MealORM) -> MixinMeal:
        entity = None
        with contextlib.suppress(ValidationError):
            entity = ComplexMeal.model_validate(entity_orm)
        with contextlib.suppress(ValidationError):
            entity = DetailedMeal.model_validate(entity_orm)
        if entity is None:
            # TODO: Make a custom exception
            raise ValueError(f"Failed to validate entity '{entity_orm}'")
        return entity

    def _entity_to_orm(self, entity: MixinMeal) -> MealORM:
        return MealORM(**entity.model_dump())
