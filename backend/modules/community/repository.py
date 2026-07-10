from uuid import UUID

from sqlalchemy.orm import Session

from modules.community.models import Community
from modules.community.schemas import (
    CommunityCreate,
    CommunityUpdate,
)


class CommunityRepository:

    @staticmethod
    def get_all(db: Session) -> list[Community]:
        return db.query(Community).all()

    @staticmethod
    def get_by_id(
        db: Session,
        community_id: UUID,
    ) -> Community | None:
        return (
            db.query(Community)
            .filter(Community.id == community_id)
            .first()
        )

    @staticmethod
    def get_by_name(
        db: Session,
        name: str,
    ) -> Community | None:
        return (
            db.query(Community)
            .filter(Community.name == name)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        data: CommunityCreate,
    ) -> Community:

        community = Community(
            **data.model_dump()
        )

        db.add(community)
        db.commit()
        db.refresh(community)

        return community
    

    @staticmethod
    def update(
        db: Session,
        community: Community,
        data: CommunityUpdate,
    ) -> Community:

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                community,
                key,
                value,
            )

        db.commit()
        db.refresh(community)

        return community
    

    @staticmethod
    def delete(db: Session, community_id: UUID):

        community = (
            db.query(Community)
            .filter(Community.id == community_id)
            .first()
        )

        if not community:
            return None

        community.is_active = False

        db.commit()
        db.refresh(community)

        return community