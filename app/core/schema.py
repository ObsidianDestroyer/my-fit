import orjson

from typing import Annotated, Optional

from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.functional_validators import BeforeValidator

FilterField = Annotated[dict, Field(min_length=0, max_length=1), BeforeValidator(orjson.loads)]
NameField = Annotated[list[str], Field(min_length=0, max_length=15), BeforeValidator(orjson.loads)]


class Filter(BaseModel):
    filter: Optional[FilterField] = None
    name: Optional[NameField] = None
