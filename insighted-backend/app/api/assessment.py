from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.assessment_schema import (
    AssessmentCreate,
    AssessmentResponse
)

from app.services.assessment_service import (
    create_assessment,
    get_assessment_by_id
)

from app.dependencies.roles import (
    get_current_teacher_record
)

from app.models.teacher import Teacher

router = APIRouter(
    prefix="/assessments",
    tags=["Assessments"]
)


@router.post(
    "/",
    response_model=AssessmentResponse
)
def create_assessment_endpoint(
    request: AssessmentCreate,
    db: Session = Depends(get_db),
    current_teacher: Teacher = Depends(
        get_current_teacher_record
    )
):

    try:

        assessment = create_assessment(
            db=db,
            classroom_id=request.classroom_id,
            teacher_id=current_teacher.id,
            title=request.title,
            description=request.description,
            assessment_type=request.assessment_type,
            total_marks=request.total_marks,
            due_date=request.due_date
        )

        return assessment

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/{assessment_id}",
    response_model=AssessmentResponse
)
def get_assessment_by_id_endpoint(
    assessment_id: int,
    db: Session = Depends(get_db),
    current_teacher: Teacher = Depends(
        get_current_teacher_record
    )
):

    try:

        assessment = get_assessment_by_id(
            db=db,
            assessment_id=assessment_id,
            teacher_id=current_teacher.id
        )

        return assessment

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )