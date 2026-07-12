from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MemberCreate(BaseModel):
    division_id: UUID
    category_id: UUID
    full_name: str
    father_name: str


class MemberUpdate(BaseModel):
    division_id: UUID | None = None
    category_id: UUID | None = None
    full_name: str | None = None
    father_name: str | None = None


class MemberResponse(BaseModel):
    id: UUID
    division_id: UUID
    category_id: UUID

    member_code: str

    full_name: str
    father_name: str

    is_active: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )