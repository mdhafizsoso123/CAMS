from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from database.base_model import BaseModel


class Community(BaseModel):
    __tablename__ = "communities"

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    divisions = relationship(
        "Division",
        back_populates="community",
        cascade="all, delete-orphan",
    )