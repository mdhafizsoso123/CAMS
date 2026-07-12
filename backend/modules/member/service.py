from uuid import UUID

from modules.member.repository import MemberRepository
from modules.member.schemas import (
    MemberCreate,
    MemberUpdate,
)


class MemberService:

    def __init__(
        self,
        repository: MemberRepository,
    ):
        self.repository = repository


    def create_member(
        self,
        data: MemberCreate,
    ):

        # Check Division
        division = self.repository.get_division(
            data.division_id,
        )

        if not division:
            raise ValueError(
                "Division not found."
            )


        # Check Category
        category = self.repository.get_category(
            data.category_id,
        )

        if not category:
            raise ValueError(
                "Category not found."
            )


        # Category belongs to same community
        if category.community_id != division.community_id:
            raise ValueError(
                "Category does not belong to selected division community."
            )


        return self.repository.create(data)



    def get_all_members(self):

        return self.repository.get_all()



    def get_member(
        self,
        member_id: UUID,
    ):

        return self.repository.get_by_id(
            member_id,
        )



    def update_member(
        self,
        member_id: UUID,
        data: MemberUpdate,
    ):

        member = self.repository.get_by_id(
            member_id,
        )

        if not member:
            return None


        if data.division_id:

            division = self.repository.get_division(
                data.division_id,
            )

            if not division:
                raise ValueError(
                    "Division not found."
                )


        if data.category_id:

            category = self.repository.get_category(
                data.category_id,
            )

            if not category:
                raise ValueError(
                    "Category not found."
                )


        return self.repository.update(
            member,
            data,
        )



    def activate_member(
        self,
        member_id: UUID,
    ):

        member = self.repository.get_by_id(
            member_id,
        )

        if not member:
            return None

        return self.repository.activate(member)



    def deactivate_member(
        self,
        member_id: UUID,
    ):

        member = self.repository.get_by_id(
            member_id,
        )

        if not member:
            return None

        return self.repository.deactivate(member)