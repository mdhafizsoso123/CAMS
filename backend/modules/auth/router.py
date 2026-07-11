from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.session import get_db

from modules.auth.service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    result = AuthService.login(
        db,
        form_data.username,
        form_data.password
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return result