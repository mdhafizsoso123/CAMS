from uuid import UUID

from modules.community.repository import CommunityRepository

from modules.division.models import Division
from modules.division.repository import DivisionRepository
from modules.division.schemas import (
    DivisionCreate,
    DivisionUpdate,
)


class DivisionService:

    def __init__(
        self,
        repository: DivisionRepository,
    ):
        self.repository = repository

    def create_division(
        self,
        data: DivisionCreate,
    ):

        if self.repository.get_by_name(data.name):
            raise ValueError(
                "Division name already exists."
            )

        if self.repository.get_by_code(data.code):
            raise ValueError(
                "Division code already exists."
            )

        community = CommunityRepository.get_first(
            self.repository.db
        )

        if not community:
            raise ValueError(
                "Community not found."
            )

        division = Division(
            name=data.name,
            code=data.code,
            description=data.description,
            community_id=community.id,
        )

        return self.repository.create(division)

    def get_all_divisions(self):
        return self.repository.get_all()

    def get_division(
        self,
        division_id: UUID,
    ):
        return self.repository.get_by_id(
            division_id
        )

    def update_division(
        self,
        division_id: UUID,
        data: DivisionUpdate,
    ):

        division = self.repository.get_by_id(
            division_id
        )

        if not division:
            return None

        if (
            data.name
            and data.name != division.name
        ):

            if self.repository.get_by_name(
                data.name
            ):
                raise ValueError(
                    "Division name already exists."
                )

            division.name = data.name

        if (
            data.code
            and data.code != division.code
        ):

            if self.repository.get_by_code(
                data.code
            ):
                raise ValueError(
                    "Division code already exists."
                )

            division.code = data.code

        if data.description is not None:
            division.description = data.description

        if data.is_active is not None:
            division.is_active = data.is_active

        self.repository.update()

        return division

    def deactivate_division(
        self,
        division_id: UUID,
    ):

        division = self.repository.get_by_id(
            division_id
        )

        if not division:
            return None

        division.is_active = False

        self.repository.update()

        return division