from fastapi import Depends, HTTPException, status

from modules.auth.dependencies import get_current_user
from modules.user.models import User, UserRole


def require_roles(*roles: UserRole):

    def permission(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

        return current_user

    return permission


require_admin = require_roles(
    UserRole.ADMIN
)

require_manager = require_roles(
    UserRole.ADMIN,
    UserRole.MANAGER
)

require_member = require_roles(
    UserRole.ADMIN,
    UserRole.MANAGER,
    UserRole.MEMBER
)