from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.database.session import get_db

from app.models.student import Student
from app.models.teacher import Teacher


def get_current_super_admin(
    current_user=Depends(get_current_user)
):
    if current_user.role != "super_admin":
        raise HTTPException(
            status_code=403,
            detail="Super Admin access required"
        )

    return current_user


def get_current_organization_admin(
    current_user=Depends(get_current_user)
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
    current_user=Depends(get_current_user)
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
    current_user=Depends(get_current_user)
):
    if current_user.role != "student":
        raise HTTPException(
            status_code=403,
            detail="Student access required"
        )

    return current_user


def get_current_student_record(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "student":
        raise HTTPException(
            status_code=403,
            detail="Student access required"
        )

    student = (
        db.query(Student)
        .filter(
            Student.user_id == current_user.id
        )
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    return student


def get_current_teacher_record(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "teacher":
        raise HTTPException(
            status_code=403,
            detail="Teacher access required"
        )

    teacher = (
        db.query(Teacher)
        .filter(
            Teacher.user_id == current_user.id
        )
        .first()
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher profile not found"
        )

    return teacher