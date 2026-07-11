from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_db

from modules.division.repository import DivisionRepository
from modules.division.schemas import (
    DivisionCreate,
    DivisionResponse,
    DivisionUpdate,
)
from modules.division.service import DivisionService


router = APIRouter(
    prefix="/divisions",
    tags=["Divisions"],
)


def get_service(
    db: Session = Depends(get_db),
):
    repository = DivisionRepository(db)
    return DivisionService(repository)


@router.post(
    "",
    response_model=DivisionResponse,
)
def create_division(
    data: DivisionCreate,
    service: DivisionService = Depends(get_service),
):
    try:
        return service.create_division(data)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[DivisionResponse],
)
def get_divisions(
    service: DivisionService = Depends(get_service),
):
    return service.get_all_divisions()


@router.get(
    "/{division_id}",
    response_model=DivisionResponse,
)
def get_division(
    division_id: UUID,
    service: DivisionService = Depends(get_service),
):
    division = service.get_division(division_id)

    if not division:
        raise HTTPException(
            status_code=404,
            detail="Division not found.",
        )

    return division


@router.put(
    "/{division_id}",
    response_model=DivisionResponse,
)
def update_division(
    division_id: UUID,
    data: DivisionUpdate,
    service: DivisionService = Depends(get_service),
):
    try:
        division = service.update_division(
            division_id,
            data,
        )

        if not division:
            raise HTTPException(
                status_code=404,
                detail="Division not found.",
            )

        return division

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.patch(
    "/{division_id}/deactivate",
    response_model=DivisionResponse,
)
def deactivate_division(
    division_id: UUID,
    service: DivisionService = Depends(get_service),
):

    division = service.deactivate_division(
        division_id
    )

    if not division:
        raise HTTPException(
            status_code=404,
            detail="Division not found."
        )

    return division