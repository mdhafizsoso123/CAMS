from sqlalchemy import Boolean, Column, Enum, String
from database.base_model import BaseModel

import enum

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"

class User(BaseModel):
    __tablename__ = "users"

    full_name = Column(
        String(150),
        nullable=False,
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
    )

    phone = Column(
        String(20),
        unique=True,
        nullable=True,
    )

    password_hash = Column(
        String(255),
        nullable=False,
    )

    role = Column(
        Enum(UserRole),
        default=UserRole.MEMBER,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )