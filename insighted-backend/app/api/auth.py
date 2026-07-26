from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth_schema import (
    RegisterRequest,
    RegisterResponse
)
from app.services.auth_service import register_user
from app.schemas.auth_schema import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import (
    login_user
)

from app.core.security import (
    create_access_token
)
from app.dependencies.auth import get_current_user
from app.schemas.user_schema import UserResponse
from app.models.user import User
from app.dependencies.roles import (
    get_current_super_admin
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=RegisterResponse
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        register_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
            organization_id=request.organization_id
        )

        return {
            "message": "User registered successfully"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = login_user(
        db,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user
@router.get("/super-admin-test")
def super_admin_test(
    current_user=Depends(
        get_current_super_admin
    )
):
    return {
        "message": "Welcome Super Admin",
        "user": current_user.name
    }