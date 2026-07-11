from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from sqlalchemy.orm import Session
from uuid import UUID

from database.session import get_db

from modules.user.repository import UserRepository
from modules.user.schemas import UserCreate, UserResponse
from modules.user.service import UserService
from modules.auth.dependencies import get_current_user
from modules.user.models import User

from core.permissions import require_admin


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)


@router.post(
    "",
    response_model=UserResponse,
)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_service),
):
    try:
        return service.create_user(data)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[UserResponse],
)
def get_users(
    current_user: User = Depends(require_admin),
    service: UserService = Depends(get_service),
):
    return service.get_all_users()


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": str(current_user.id),
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role.value
    }


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: UUID,
    service: UserService = Depends(get_service),
):
    user = service.get_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    return user


@router.delete(
    "/{user_id}",
    response_model=UserResponse,
)
def delete_user(
    user_id: UUID,
    service: UserService = Depends(get_service),
):
    user = service.delete_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )

    return user


