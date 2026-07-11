from sqlalchemy.orm import Session

from modules.user.models import User
from modules.user.password import verify_password
from modules.auth.jwt import create_access_token


class AuthService:

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash
        ):
            return None


        token = create_access_token(
            {
                "user_id": str(user.id),
                "role": user.role.value
            }
        )


        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": str(user.id),
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role.value
            }
        }