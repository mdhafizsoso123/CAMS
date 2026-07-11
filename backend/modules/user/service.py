from uuid import UUID

from modules.user.models import User
from modules.user.repository import UserRepository
from modules.user.schemas import UserCreate
from modules.user.password import hash_password


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, data: UserCreate) -> User:

        existing_user = self.repository.get_by_email(data.email)

        if existing_user:
            raise ValueError("Email already registered.")

        user = User(
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            password_hash=hash_password(data.password),
            role=data.role,
        )

        return self.repository.create(user)

    def get_user(self, user_id: UUID):
        return self.repository.get_by_id(user_id)

    def get_all_users(self):
        return self.repository.get_all()

    def delete_user(self, user_id: UUID):

        user = self.repository.get_by_id(user_id)

        if not user:
            return None

        self.repository.delete(user)

        return user