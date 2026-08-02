from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.models.submission_answer import SubmissionAnswer


def review_submission_answer(
    db: Session,
    submission_answer_id: int,
    marks_obtained: int,
    feedback: str | None = None
):

    answer = (
        db.query(SubmissionAnswer)
        .filter(
            SubmissionAnswer.id == submission_answer_id
        )
        .first()
    )

    if not answer:
        raise ValueError(
            "Submission answer not found"
        )

    answer.marks_obtained = marks_obtained
    answer.feedback = feedback
    answer.evaluated_at = datetime.now(
        timezone.utc
    )

    submission = answer.submission

    total_score = 0

    for submission_answer in submission.answers:

        total_score += (
            submission_answer.marks_obtained
            or 0
        )

    submission.total_score = total_score

    db.commit()
    db.refresh(answer)

    return answer