from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)

from app.services.student_service import (
    create_student
)
from app.dependencies.roles import (
    get_current_organization_admin
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse
)
def create_student_endpoint(
    request: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(
        get_current_organization_admin
    )
):
    try:
        student = create_student(
            db=db,
            user_id=request.user_id,
            organization_id=request.organization_id,
            roll_number=request.roll_number,
            class_name=request.class_name,
            section=request.section
        )

        return student

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )