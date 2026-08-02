print("REVIEW ROUTER LOADED")
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.review_schema import (
    ReviewCreate
)

from app.schemas.submission_answer_schema import (
    SubmissionAnswerResponse
)

from app.services.review_service import (
    review_submission_answer
)

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post(
    "/{submission_answer_id}",
    response_model=SubmissionAnswerResponse
)
def review_submission_answer_endpoint(
    submission_answer_id: int,
    request: ReviewCreate,
    db: Session = Depends(get_db)
):

    try:

        answer = review_submission_answer(
            db=db,
            submission_answer_id=submission_answer_id,
            marks_obtained=request.marks_obtained,
            feedback=request.feedback
        )

        return answer

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )