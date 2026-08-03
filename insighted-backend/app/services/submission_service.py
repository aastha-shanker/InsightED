from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.models.assessment import Assessment
from app.models.student import Student


def create_submission(
    db: Session,
    assessment_id: int,
    student_id: int
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

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if not student:
        raise ValueError(
            "Student not found"
        )

    existing_submission = (
        db.query(Submission)
        .filter(
            Submission.assessment_id == assessment_id,
            Submission.student_id == student_id
        )
        .first()
    )

    if existing_submission:
        raise ValueError(
            "Submission already exists for this assessment"
        )

    submission = Submission(
        assessment_id=assessment_id,
        student_id=student_id
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return submission

def get_submission_by_id(
    db: Session,
    submission_id: int
):

    submission = (
        db.query(Submission)
        .filter(
            Submission.id == submission_id
        )
        .first()
    )

    if not submission:
        raise ValueError(
            "Submission not found"
        )

    return submission


def get_submissions_by_student(
    db: Session,
    student_id: int
):

    student = (
        db.query(Student)
        .filter(
            Student.id == student_id
        )
        .first()
    )

    if not student:
        raise ValueError(
            "Student not found"
        )

    submissions = (
        db.query(Submission)
        .filter(
            Submission.student_id == student_id
        )
        .all()
    )

    return submissions


def get_submissions_by_assessment(
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

    submissions = (
        db.query(Submission)
        .filter(
            Submission.assessment_id == assessment_id
        )
        .all()
    )

    return submissions