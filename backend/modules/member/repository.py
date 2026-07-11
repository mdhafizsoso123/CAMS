from uuid import UUID

from sqlalchemy.orm import Session

from modules.member.models import Member
from modules.member.schemas import (
    MemberCreate,
    MemberUpdate,
)

from modules.division.models import Division


class MemberRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Member]:
        return self.db.query(Member).all()

    def get_by_id(
        self,
        member_id: UUID,
    ) -> Member | None:

        return (
            self.db.query(Member)
            .filter(Member.id == member_id)
            .first()
        )

    def get_by_member_code(
        self,
        member_code: str,
    ) -> Member | None:

        return (
            self.db.query(Member)
            .filter(Member.member_code == member_code)
            .first()
        )

    def get_division(
        self,
        division_id: UUID,
    ) -> Division | None:

        return (
            self.db.query(Division)
            .filter(
                Division.id == division_id,
                Division.is_active == True,
            )
            .first()
        )

    def generate_member_code(
        self,
        division: Division,
    ) -> str:

        last_member = (
            self.db.query(Member)
            .filter(Member.division_id == division.id)
            .order_by(Member.member_code.desc())
            .first()
        )

        if not last_member:
            return f"{division.code}-0001"

        last_number = int(
            last_member.member_code.split("-")[1]
        )

        next_number = last_number + 1

        return f"{division.code}-{next_number:04d}"

    def create(
        self,
        data: MemberCreate,
    ) -> Member:

        division = self.get_division(
            data.division_id,
        )

        member = Member(
            division_id=data.division_id,
            member_code=self.generate_member_code(
                division,
            ),
            full_name=data.full_name,
            father_name=data.father_name,
        )

        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)

        return member

    def update(
        self,
        member: Member,
        data: MemberUpdate,
    ) -> Member:

        update_data = data.model_dump(
            exclude_unset=True,
        )

        for key, value in update_data.items():
            setattr(member, key, value)

        self.db.commit()
        self.db.refresh(member)

        return member

    def deactivate(
        self,
        member: Member,
    ) -> Member:

        member.is_active = False

        self.db.commit()
        self.db.refresh(member)

        return member

    def activate(
        self,
        member: Member,
    ) -> Member:

        member.is_active = True

        self.db.commit()
        self.db.refresh(member)

        return member