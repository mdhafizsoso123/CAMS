from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from database.session import get_db

from modules.member.repository import MemberRepository
from modules.member.schemas import (
    MemberCreate,
    MemberUpdate,
    MemberResponse,
)
from modules.member.service import MemberService

from modules.auth.dependencies import (
    get_current_user,
)
from core.permissions import (
    require_admin,
)


router = APIRouter(
    prefix="/members",
    tags=["Members"],
)


def get_service(
    db: Session = Depends(get_db),
):

    repository = MemberRepository(db)

    return MemberService(repository)


@router.post(
    "",
    response_model=MemberResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_admin),
    ],
)
def create_member(
    data: MemberCreate,
    service: MemberService = Depends(get_service),
):

    try:
        return service.create_member(data)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[MemberResponse],
    dependencies=[
        Depends(get_current_user),
    ],
)
def get_members(
    service: MemberService = Depends(get_service),
):

    return service.get_all_members()


@router.get(
    "/{member_id}",
    response_model=MemberResponse,
    dependencies=[
        Depends(get_current_user),
    ],
)
def get_member(
    member_id: UUID,
    service: MemberService = Depends(get_service),
):

    member = service.get_member(
        member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found.",
        )

    return member


@router.put(
    "/{member_id}",
    response_model=MemberResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_admin),
    ],
)
def update_member(
    member_id: UUID,
    data: MemberUpdate,
    service: MemberService = Depends(get_service),
):

    member = service.update_member(
        member_id,
        data,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found.",
        )

    return member


@router.patch(
    "/{member_id}/activate",
    response_model=MemberResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_admin),
    ],
)
def activate_member(
    member_id: UUID,
    service: MemberService = Depends(get_service),
):

    member = service.activate_member(
        member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found.",
        )

    return member


@router.patch(
    "/{member_id}/deactivate",
    response_model=MemberResponse,
    dependencies=[
        Depends(get_current_user),
        Depends(require_admin),
    ],
)
def deactivate_member(
    member_id: UUID,
    service: MemberService = Depends(get_service),
):

    member = service.deactivate_member(
        member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found.",
        )

    return member