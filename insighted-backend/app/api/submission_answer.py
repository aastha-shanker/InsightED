from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.submission_answer_schema import (
    SubmissionAnswerCreate,
    SubmissionAnswerResponse
)

from app.services.submission_answer_service import (
    create_submission_answer,
    get_answers_by_submission
)

from app.dependencies.roles import (
    get_current_student_record
)

from app.models.student import Student

router = APIRouter(
    prefix="/submission-answers",
    tags=["Submission Answers"]
)


@router.post(
    "/",
    response_model=SubmissionAnswerResponse
)
def create_submission_answer_endpoint(
    request: SubmissionAnswerCreate,
    db: Session = Depends(get_db),
    current_student: Student = Depends(
        get_current_student_record
    )
):

    try:
        submission_answer = create_submission_answer(
            db=db,
            submission_id=request.submission_id,
            question_id=request.question_id,
            answer_text=request.answer_text,
            file_url=request.file_url,
            current_student_id=current_student.id
        )

        return submission_answer

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
        
@router.get(
    "/submission/{submission_id}",
    response_model=list[SubmissionAnswerResponse]
)
def get_answers_by_submission_endpoint(
    submission_id: int,
    db: Session = Depends(get_db),
    current_student: Student = Depends(
        get_current_student_record
    )
):

    try:

        answers = get_answers_by_submission(
            db=db,
            submission_id=submission_id,
            current_student_id=current_student.id
        )

        return answers

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )