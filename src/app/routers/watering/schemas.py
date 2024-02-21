from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, Field, BaseModel, field_validator


class WateringBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class WateringCreate(WateringBase):
    plant_id: int
    user_id: int
    timestamp: Optional[datetime]
    fertilizer: bool = Field(default=False)

    @field_validator("plant_id")
    def validate_plant_id(cls, v):
        assert v > 0
        return v

    @field_validator("user_id")
    def validate_user_id(cls, v):
        assert v > 0
        return v


class WateringUpdate(WateringBase):
    ...


class WateringQuerySchema(WateringBase):
    """to do"""

    ...
