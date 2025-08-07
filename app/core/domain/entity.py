from pydantic.main import BaseModel
from pydantic.fields import Field
from pydantic.config import ConfigDict

from app.core.domain.values import ID


class DomainEntity(BaseModel):
    id: ID = Field(default_factory=ID)
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)
