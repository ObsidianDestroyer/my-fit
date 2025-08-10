import uuid

from dataclasses import dataclass

from typing import Optional

from sqlalchemy.types import UUID, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import ORMBase
from app.core.domain.values import DateTime as DateTimeValue


@dataclass(frozen=True)
class ColumnSpec:
    INDEXABLE = dict(index=True)
    NULLABLE = dict(nullable=True)


class MealORM(ORMBase):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, **ColumnSpec.INDEXABLE)
    datetime: Mapped[DateTimeValue] = mapped_column(DateTime, server_default=DateTimeValue)

    mass_grams: Mapped[float] = mapped_column(Float)
    calories: Mapped[float] = mapped_column(Float, **ColumnSpec.NULLABLE)
    protein: Mapped[float] = mapped_column(Float, **ColumnSpec.NULLABLE)
    fat: Mapped[float] = mapped_column(Float, **ColumnSpec.NULLABLE)
    carbs: Mapped[float] = mapped_column(Float, **ColumnSpec.NULLABLE)

    image_url: Mapped[float] = mapped_column(Float, **ColumnSpec.NULLABLE)


