from sqlalchemy import (
    Boolean,
    ForeignKey,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.base_model import BaseModel


class MemberCategory(BaseModel):
    __tablename__ = "member_categories"

    community_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("communities.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    community = relationship(
        "Community",
        back_populates="member_categories",
    )

    members = relationship(
        "Member",
        back_populates="category",
    )