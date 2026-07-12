import uuid

from sqlalchemy import (
    String,
    Boolean,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.base_model import BaseModel


class Member(BaseModel):

    __tablename__ = "members"

    division_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("divisions.id"),
        nullable=False,
    )

    category_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("member_categories.id"),
        nullable=False,
    )

    member_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    father_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    division = relationship(
        "Division",
        back_populates="members",
    )

    category = relationship(
        "MemberCategory",
        back_populates="members",
    )