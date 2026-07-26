from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.assessment import Assessment


def create_question(
    db: Session,
    assessment_id: int,
    question_text: str,
    question_type: str,
    marks: int
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

    question = Question(
        assessment_id=assessment_id,
        question_text=question_text,
        question_type=question_type,
        marks=marks
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question