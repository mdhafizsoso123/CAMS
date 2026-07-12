from uuid import UUID

from fastapi import HTTPException, status

from modules.community.repository import CommunityRepository

from .repository import MemberCategoryRepository
from .schemas import (
    MemberCategoryCreate,
    MemberCategoryUpdate,
)


class MemberCategoryService:

    def __init__(self, db):

        self.repository = MemberCategoryRepository(db)
        self.community_repository = CommunityRepository


    def create_category(
        self,
        data: MemberCategoryCreate,
    ):

        community = self.community_repository.get_by_id(
            self.repository.db,
            data.community_id,
        )

        if not community:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Community not found",
            )

        if not community.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Community is inactive",
            )


        existing = self.repository.get_by_name(
            data.community_id,
            data.name,
        )

        if existing:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category already exists",
            )


        return self.repository.create(data)



    def get_categories(self):

        return self.repository.get_all()



    def get_category(
        self,
        category_id: UUID,
    ):

        category = self.repository.get_by_id(
            category_id,
        )

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        return category



    def update_category(
        self,
        category_id: UUID,
        data: MemberCategoryUpdate,
    ):

        category = self.get_category(
            category_id,
        )


        if data.name is not None:

            existing = self.repository.get_by_name(
                category.community_id,
                data.name,
            )


            if (
                existing
                and existing.id != category.id
            ):

                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Category already exists",
                )


        return self.repository.update(
            category,
            data,
        )



    def activate_category(
        self,
        category_id: UUID,
    ):

        category = self.get_category(
            category_id,
        )

        return self.repository.activate(
            category,
        )



    def deactivate_category(
        self,
        category_id: UUID,
    ):

        category = self.get_category(
            category_id,
        )

        return self.repository.deactivate(
            category,
        )