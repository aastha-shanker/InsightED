from fastapi import Depends, HTTPException

from app.dependencies.auth import (
    get_current_user
)

def get_current_super_admin(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role != "super_admin":
        raise HTTPException(
            status_code=403,
            detail="Super Admin access required"
        )

    return current_user

def get_current_organization_admin(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role not in [
        "organization_admin",
        "super_admin"
    ]:
        raise HTTPException(
            status_code=403,
            detail="Organization Admin access required"
        )

    return current_user
def get_current_teacher(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role not in [
        "teacher",
        "organization_admin",
        "super_admin"
    ]:
        raise HTTPException(
            status_code=403,
            detail="Teacher access required"
        )

    return current_user


def get_current_student(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role != "student":
        raise HTTPException(
            status_code=403,
            detail="Student access required"
        )

    return current_user