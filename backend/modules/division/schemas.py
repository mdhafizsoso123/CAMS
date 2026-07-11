from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DivisionCreate(BaseModel):
    name: str
    code: str
    description: str | None = None


class DivisionUpdate(BaseModel):
    name: str | None = None
    code: str | None = None
    description: str | None = None
    is_active: bool | None = None


class DivisionResponse(BaseModel):
    id: UUID
    name: str
    code: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )