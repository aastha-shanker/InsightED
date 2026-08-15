from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.dashboard_schema import (
    TeacherDashboardResponse,
    StudentDashboardResponse
)

from app.services.dashboard_service import (
    get_teacher_dashboard,
    get_student_dashboard
)
from app.dependencies.roles import (
    get_current_teacher_record,
    get_current_student_record
)

from app.models.teacher import Teacher
from app.models.student import Student

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/teacher/{teacher_id}",
    response_model=TeacherDashboardResponse
)
def get_teacher_dashboard_endpoint(
    teacher_id: int,
    db: Session = Depends(get_db),
    current_teacher: Teacher = Depends(
        get_current_teacher_record
    )
):
    if current_teacher.id != teacher_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    try:

        dashboard = get_teacher_dashboard(
            db=db,
            teacher_id=teacher_id
        )

        return dashboard

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
        
@router.get(
    "/student/{student_id}",
    response_model=StudentDashboardResponse
)
def get_student_dashboard_endpoint(
    student_id: int,
    db: Session = Depends(get_db),
    current_student: Student = Depends(
        get_current_student_record
    )
):
    if current_student.id != student_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )
    try:

        dashboard = get_student_dashboard(
            db=db,
            student_id=student_id
        )

        return dashboard

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )