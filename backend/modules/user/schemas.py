from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from modules.user.models import UserRole


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str
    role: UserRole = UserRole.MEMBER


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None
    role: UserRole | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    full_name: str
    email: EmailStr
    phone: str | None
    role: UserRole
    is_active: bool