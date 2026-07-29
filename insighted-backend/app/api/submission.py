from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.submission_schema import (
    SubmissionCreate,
    SubmissionResponse
)

from app.services.submission_service import (
    create_submission
)

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)


@router.post(
    "/",
    response_model=SubmissionResponse
)
def create_submission_endpoint(
    request: SubmissionCreate,
    db: Session = Depends(get_db)
):

    try:
        submission = create_submission(
            db=db,
            assessment_id=request.assessment_id,
            student_id=request.student_id
        )

        return submission

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )