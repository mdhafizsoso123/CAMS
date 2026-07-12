from uuid import UUID

from sqlalchemy.orm import Session

from .models import MemberCategory
from .schemas import (
    MemberCategoryCreate,
    MemberCategoryUpdate,
)


class MemberCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(
        self,
        category_id: UUID,
    ) -> MemberCategory | None:

        return (
            self.db.query(MemberCategory)
            .filter(MemberCategory.id == category_id)
            .first()
        )

    def get_by_name(
        self,
        community_id: UUID,
        name: str,
    ) -> MemberCategory | None:

        return (
            self.db.query(MemberCategory)
            .filter(
                MemberCategory.community_id == community_id,
                MemberCategory.name == name,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[MemberCategory]:

        return (
            self.db.query(MemberCategory)
            .order_by(MemberCategory.name)
            .all()
        )

    def create(
        self,
        data: MemberCategoryCreate,
    ) -> MemberCategory:

        category = MemberCategory(
            community_id=data.community_id,
            name=data.name,
            description=data.description,
            is_active=True,
        )

        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update(
        self,
        category: MemberCategory,
        data: MemberCategoryUpdate,
    ) -> MemberCategory:

        if data.name is not None:
            category.name = data.name

        if data.description is not None:
            category.description = data.description

        self.db.commit()
        self.db.refresh(category)

        return category

    def activate(
        self,
        category: MemberCategory,
    ) -> MemberCategory:

        category.is_active = True

        self.db.commit()
        self.db.refresh(category)

        return category

    def deactivate(
        self,
        category: MemberCategory,
    ) -> MemberCategory:

        category.is_active = False

        self.db.commit()
        self.db.refresh(category)

        return category