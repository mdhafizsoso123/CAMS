from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MemberCategoryCreate(BaseModel):
    community_id: UUID
    name: str
    description: str | None = None


class MemberCategoryUpdate(BaseModel):
    community_id: UUID | None = None
    name: str | None = None
    description: str | None = None


class MemberCategoryResponse(BaseModel):
    id: UUID
    community_id: UUID
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )