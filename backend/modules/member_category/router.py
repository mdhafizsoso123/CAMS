from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from core.permissions import require_admin

from .schemas import (
    MemberCategoryCreate,
    MemberCategoryUpdate,
    MemberCategoryResponse,
)
from .service import MemberCategoryService


router = APIRouter(
    prefix="/member-categories",
    tags=["Member Categories"],
)


@router.post(
    "",
    response_model=MemberCategoryResponse,
    dependencies=[Depends(require_admin)],
)
def create_category(
    data: MemberCategoryCreate,
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.create_category(data)


@router.get(
    "",
    response_model=list[MemberCategoryResponse],
    dependencies=[Depends(require_admin)],
)
def get_categories(
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.get_categories()


@router.get(
    "/{category_id}",
    response_model=MemberCategoryResponse,
    dependencies=[Depends(require_admin)],
)
def get_category(
    category_id: UUID,
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.get_category(category_id)


@router.put(
    "/{category_id}",
    response_model=MemberCategoryResponse,
    dependencies=[Depends(require_admin)],
)
def update_category(
    category_id: UUID,
    data: MemberCategoryUpdate,
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.update_category(
        category_id,
        data,
    )


@router.patch(
    "/{category_id}/activate",
    response_model=MemberCategoryResponse,
    dependencies=[Depends(require_admin)],
)
def activate_category(
    category_id: UUID,
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.activate_category(category_id)


@router.patch(
    "/{category_id}/deactivate",
    response_model=MemberCategoryResponse,
    dependencies=[Depends(require_admin)],
)
def deactivate_category(
    category_id: UUID,
    db: Session = Depends(get_db),
):

    service = MemberCategoryService(db)

    return service.deactivate_category(category_id)