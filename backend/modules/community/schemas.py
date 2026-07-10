from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class CommunityCreate(BaseModel):
    name: str
    description: str | None = None
    address: str | None = None
    phone: str | None = None
    email: EmailStr | None = None


class CommunityUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    address: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


class CommunityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str | None
    address: str | None
    phone: str | None
    email: EmailStr | None
    is_active: bool

    created_at: datetime
    updated_at: datetime