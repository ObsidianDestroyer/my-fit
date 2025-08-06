from app.domain.entities import ComplexMeal, DetailedMeal


class ComplexMealResponse(ComplexMeal):
    mass_grams: float
    calories: float | None = None
    protein: float | None = None
    fat: float | None = None
    carbs: float | None = None
    image_url: str | None = None


class DetailedMealResponse(DetailedMeal):
    pass
