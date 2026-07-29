from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.models.submission_answer import SubmissionAnswer


def evaluate_submission(
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

    answers = (
        db.query(SubmissionAnswer)
        .filter(
            SubmissionAnswer.submission_id == submission_id
        )
        .all()
    )

    total_score = 0

    for answer in answers:

        question = answer.question

        if (
          question.question_type.lower() == "mcq"
          and answer.answer_text.strip().upper()
          == question.correct_answer.strip().upper()
        ):

            answer.marks_obtained = question.marks

        elif question.question_type.lower() == "mcq":

            answer.marks_obtained = 0

        total_score += (
            answer.marks_obtained or 0
        )

    submission.total_score = total_score
    submission.status = "evaluated"

    db.commit()

    return submission