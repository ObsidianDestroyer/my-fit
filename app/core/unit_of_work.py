from typing import Self
from types import TracebackType

from abc import ABC

from app.core.repository import IRepository


class BaseUOW(ABC):
    repo: IRepository

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException | None,
        exc_tb: TracebackType,
    ) -> None:
        pass
