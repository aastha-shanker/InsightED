from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.teacher_schema import (
    TeacherCreate,
    TeacherResponse
)

from app.services.teacher_service import (
    create_teacher
)

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@router.post(
    "/",
    response_model=TeacherResponse
)
def create_teacher_endpoint(
    request: TeacherCreate,
    db: Session = Depends(get_db)
):
    try:
        teacher = create_teacher(
            db=db,
            user_id=request.user_id,
            organization_id=request.organization_id,
            employee_id=request.employee_id,
            department=request.department,
            designation=request.designation
        )

        return teacher

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )