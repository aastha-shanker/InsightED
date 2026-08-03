from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.dashboard_schema import (
    TeacherDashboardResponse
)

from app.services.dashboard_service import (
    get_teacher_dashboard
)

from app.schemas.dashboard_schema import (
    TeacherDashboardResponse,
    StudentDashboardResponse
)

from app.services.dashboard_service import (
    get_teacher_dashboard,
    get_student_dashboard
)

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
    db: Session = Depends(get_db)
):

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
    db: Session = Depends(get_db)
):

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