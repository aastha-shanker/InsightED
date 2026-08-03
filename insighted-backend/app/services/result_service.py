from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.models.student import Student

def get_result_by_submission(
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
  
def get_results_by_student(
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