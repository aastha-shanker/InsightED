from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.assessment import Assessment
from app.models.classroom import Classroom


def create_question(
    db: Session,
    teacher_id: int,
    assessment_id: int,
    question_text: str,
    question_type: str,
    marks: int,
    option_a: str | None = None,
    option_b: str | None = None,
    option_c: str | None = None,
    option_d: str | None = None,
    correct_answer: str | None = None
):

    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.id == assessment_id
        )
        .first()
    )

    if not assessment:
        raise ValueError(
            "Assessment not found"
        )

    classroom = (
        db.query(Classroom)
        .filter(
            Classroom.id == assessment.classroom_id
        )
        .first()
    )

    if not classroom:
        raise ValueError(
            "Classroom not found"
        )

    if classroom.teacher_id != teacher_id:
        raise ValueError(
            "You can only add questions to your own assessments"
        )

    question = Question(
        assessment_id=assessment_id,
        question_text=question_text,
        question_type=question_type,
        marks=marks,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
        correct_answer=correct_answer
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question


def get_questions_by_assessment(
    db: Session,
    assessment_id: int
):

    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.id == assessment_id
        )
        .first()
    )

    if not assessment:
        raise ValueError(
            "Assessment not found"
        )

    questions = (
        db.query(Question)
        .filter(
            Question.assessment_id == assessment_id
        )
        .all()
    )

    return questions