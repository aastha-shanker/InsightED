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
    create_assessment
)

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
    db: Session = Depends(get_db)
):

    try:
        assessment = create_assessment(
            db=db,
            classroom_id=request.classroom_id,
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