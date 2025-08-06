from typing import Annotated

from datetime import datetime, UTC
from uuid import uuid4

from pydantic.fields import Field
from pydantic.types import UUID4, AwareDatetime

ID = Annotated[UUID4, Field(default_factory=uuid4, frozen=True)]
DateTime = Annotated[AwareDatetime, Field(default_factory=lambda: datetime.now(tz=UTC))]
