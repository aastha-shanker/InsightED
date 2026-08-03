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
    create_submission,
    get_submission_by_id,
    get_submissions_by_student,
    get_submissions_by_assessment
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
        
@router.get(
    "/{submission_id}",
    response_model=SubmissionResponse
)
def get_submission_by_id_endpoint(
    submission_id: int,
    db: Session = Depends(get_db)
):

    try:

        submission = get_submission_by_id(
            db=db,
            submission_id=submission_id
        )

        return submission

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get(
    "/student/{student_id}",
    response_model=list[SubmissionResponse]
)
def get_submissions_by_student_endpoint(
    student_id: int,
    db: Session = Depends(get_db)
):

    try:

        submissions = get_submissions_by_student(
            db=db,
            student_id=student_id
        )

        return submissions

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
        
@router.get(
    "/assessment/{assessment_id}",
    response_model=list[SubmissionResponse]
)
def get_submissions_by_assessment_endpoint(
    assessment_id: int,
    db: Session = Depends(get_db)
):

    try:

        submissions = get_submissions_by_assessment(
            db=db,
            assessment_id=assessment_id
        )

        return submissions

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )