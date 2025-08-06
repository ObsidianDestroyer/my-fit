from typing import Optional

from pydantic.main import BaseModel

from app.core.domain.values import ID, DateTime


class BaseMeal(BaseModel):
    id: ID
    datetime: DateTime


class BaseMealStructure(BaseModel):
    mass_grams: float
    calories: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    carbs: Optional[float] = None
    image_url: Optional[str] = None


class ComplexMeal(BaseMeal, BaseMealStructure):
    pass


class MealDetails(BaseMealStructure):
    pass


class DetailedMeal(BaseMeal):
    items: list[MealDetails]
