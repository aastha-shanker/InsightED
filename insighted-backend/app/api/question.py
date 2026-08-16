from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.question_schema import (
    QuestionCreate,
    QuestionResponse
)

from app.services.question_service import (
    create_question,
    get_questions_by_assessment
)

from app.dependencies.roles import (
    get_current_teacher_record
)

from app.models.teacher import Teacher

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post(
    "/",
    response_model=QuestionResponse
)
def create_question_endpoint(
    request: QuestionCreate,
    db: Session = Depends(get_db),
    current_teacher: Teacher = Depends(
        get_current_teacher_record
    )
):

    try:

        question = create_question(
            db=db,
            teacher_id=current_teacher.id,
            assessment_id=request.assessment_id,
            question_text=request.question_text,
            question_type=request.question_type,
            marks=request.marks,
            option_a=request.option_a,
            option_b=request.option_b,
            option_c=request.option_c,
            option_d=request.option_d,
            correct_answer=request.correct_answer
        )

        return question

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/assessment/{assessment_id}",
    response_model=list[QuestionResponse]
)
def get_questions_by_assessment_endpoint(
    assessment_id: int,
    db: Session = Depends(get_db)
):

    try:

        questions = get_questions_by_assessment(
            db=db,
            assessment_id=assessment_id
        )

        return questions

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )