from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.classroom_schema import (
    ClassroomCreate,
    ClassroomResponse,
    JoinClassroomRequest,
    ClassroomListResponse
)

from app.services.classroom_service import (
    create_classroom,
    join_classroom,
    get_student_classrooms
)

router = APIRouter(
    prefix="/classrooms",
    tags=["Classrooms"]
)

@router.post(
    "/",
    response_model=ClassroomResponse
)
def create_classroom_endpoint(
    request: ClassroomCreate,
    db: Session = Depends(get_db)
):

    try:
        classroom = create_classroom(
            db=db,
            teacher_id=request.teacher_id,
            organization_id=request.organization_id,
            name=request.name
        )

        return classroom

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/join")
def join_classroom_endpoint(
    request: JoinClassroomRequest,
    db: Session = Depends(get_db)
):

    try:
        enrollment = join_classroom(
            db=db,
            student_id=request.student_id,
            join_code=request.join_code
        )

        return {
            "message": "Joined classroom successfully",
            "enrollment_id": enrollment.id
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.get(
    "/student/{student_id}",
    response_model=list[ClassroomListResponse]
)
def get_student_classrooms_endpoint(
    student_id: int,
    db: Session = Depends(get_db)
):

    try:
        return get_student_classrooms(
            db=db,
            student_id=student_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )