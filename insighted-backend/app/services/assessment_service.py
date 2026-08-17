from sqlalchemy.orm import Session

from app.models.assessment import Assessment
from app.models.classroom import Classroom


def create_assessment(
    db: Session,
    classroom_id: int,
    teacher_id: int,
    title: str,
    description: str,
    assessment_type: str,
    total_marks: int,
    due_date
):

    classroom = (
        db.query(Classroom)
        .filter(
            Classroom.id == classroom_id
        )
        .first()
    )

    if not classroom:
        raise ValueError(
            "Classroom not found"
        )

    if classroom.teacher_id != teacher_id:
        raise ValueError(
            "You do not own this classroom"
        )

    assessment = Assessment(
        classroom_id=classroom_id,
        title=title,
        description=description,
        assessment_type=assessment_type,
        total_marks=total_marks,
        due_date=due_date
    )

    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return assessment


def get_assessment_by_id(
    db: Session,
    assessment_id: int,
    teacher_id: int
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

    if classroom.teacher_id != teacher_id:
        raise ValueError(
            "Access denied"
        )

    return assessment