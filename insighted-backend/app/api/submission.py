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

from app.dependencies.roles import (
    get_current_student_record,
    get_current_teacher_record
)

from app.models.student import Student
from app.models.teacher import Teacher

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
    db: Session = Depends(get_db),
    current_student: Student = Depends(
        get_current_student_record
    )
):

    try:

        submission = create_submission(
            db=db,
            assessment_id=request.assessment_id,
            student_id=current_student.id
        )

        return submission

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.get(
    "/my",
    response_model=list[SubmissionResponse]
)
def get_my_submissions_endpoint(
    db: Session = Depends(get_db),
    current_student: Student = Depends(
        get_current_student_record
    )
):

    try:

        submissions = get_submissions_by_student(
            db=db,
            student_id=current_student.id
        )

        return submissions

    except ValueError as e:

        raise HTTPException(
            status_code=404,
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
    "/assessment/{assessment_id}",
    response_model=list[SubmissionResponse]
)
def get_submissions_by_assessment_endpoint(
    assessment_id: int,
    db: Session = Depends(get_db),
    current_teacher: Teacher = Depends(
        get_current_teacher_record
    )
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