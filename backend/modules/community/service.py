from sqlalchemy.orm import Session

from modules.community.repository import CommunityRepository
from modules.community.schemas import CommunityCreate, CommunityUpdate


class CommunityService:

    @staticmethod
    def get_all(db: Session):
        return CommunityRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, community_id):
        return CommunityRepository.get_by_id(db, community_id)

    @staticmethod
    def create(db: Session, data: CommunityCreate):

        existing = CommunityRepository.get_by_name(
            db,
            data.name,
        )

        if existing:
            raise ValueError("Community already exists.")

        return CommunityRepository.create(db, data)
    
    @staticmethod
    def update(
        db: Session,
        community_id,
        data: CommunityUpdate,
    ):

        community = CommunityRepository.get_by_id(
            db,
            community_id,
        )

        if not community:
            raise ValueError(
                "Community not found."
            )

        if data.name:

            existing = CommunityRepository.get_by_name(
                db,
                data.name,
            )

            if (
                existing
                and existing.id != community.id
            ):
                raise ValueError(
                    "Community already exists."
                )

        return CommunityRepository.update(
            db,
            community,
            data,
        )
    

    @staticmethod
    def delete(db: Session, community_id):

        community = CommunityRepository.delete(
            db,
            community_id,
        )

        if not community:
            raise ValueError("Community not found.")

        return community
