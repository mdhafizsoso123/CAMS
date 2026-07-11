import uuid

from sqlalchemy import (
    String,
    ForeignKey,
    Boolean
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base_model import BaseModel


class Division(BaseModel):

    __tablename__ = "divisions"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    community_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("communities.id"),
        nullable=False,
    )

    community = relationship(
        "Community",
        back_populates="divisions",
    )

    members = relationship(
        "Member",
        back_populates="division",
        cascade="all, delete-orphan",
    )

    code: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )