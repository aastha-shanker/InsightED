from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.evaluation_service import (
    evaluate_submission
)

from app.schemas.submission_schema import (
    SubmissionResponse
)
from app.dependencies.roles import (
    get_current_teacher
)

router = APIRouter(
    prefix="/evaluations",
    tags=["Evaluations"]
)


@router.post(
    "/{submission_id}",
    response_model=SubmissionResponse
)
def evaluate_submission_endpoint(
    submission_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
    get_current_teacher
)
    
):

    try:

        submission = evaluate_submission(
            db=db,
            submission_id=submission_id
        )

        return submission

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )