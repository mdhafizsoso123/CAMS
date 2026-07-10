from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.dependencies import get_db

from .schemas import (
    CommunityCreate,
    CommunityUpdate,
    CommunityResponse,
)

from .service import CommunityService

router = APIRouter(
    prefix="/communities",
    tags=["Community"],
)



@router.post(
    "/",
    response_model=CommunityResponse,
    status_code=201,
)
def create_community(
    data: CommunityCreate,
    db: Session = Depends(get_db),
):
    try:
        return CommunityService.create(db, data)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[CommunityResponse],
)
def get_all_communities(
    db: Session = Depends(get_db),
):
    return CommunityService.get_all(db)


@router.get(
    "/{community_id}",
    response_model=CommunityResponse,
)
def get_community(
    community_id: UUID,
    db: Session = Depends(get_db),
):
    community = CommunityService.get_by_id(
        db,
        community_id,
    )

    if not community:
        raise HTTPException(
            status_code=404,
            detail="Community not found.",
        )

    return community

@router.put(
    "/{community_id}",
    response_model=CommunityResponse,
)
def update_community(
    community_id: UUID,
    data: CommunityUpdate,
    db: Session = Depends(get_db),
):

    try:

        return CommunityService.update(
            db,
            community_id,
            data,
        )

    except ValueError as e:

        if str(e) == "Community not found.":

            raise HTTPException(
                status_code=404,
                detail=str(e),
            )

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{community_id}",
    response_model=CommunityResponse,
)
def delete_community(
    community_id: UUID,
    db: Session = Depends(get_db),
):

    try:
        return CommunityService.delete(
            db,
            community_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )