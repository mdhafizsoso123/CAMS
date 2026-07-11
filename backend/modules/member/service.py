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

        division = self.repository.get_division(
            data.division_id,
        )

        if not division:
            raise ValueError(
                "Division not found."
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