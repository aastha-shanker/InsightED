import datetime

from sqlalchemy.orm import Session

from app.models.submission_answer import SubmissionAnswer
from app.models.submission import Submission
from app.models.question import Question


def create_submission_answer(
    db: Session,
    submission_id: int,
    question_id: int,
    answer_text: str | None,
    file_url: str | None,
    current_student_id: int
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
        
    if submission.student_id != current_student_id:
        raise ValueError(
            "You can only answer your own submissions"
    )

    question = (
        db.query(Question)
        .filter(
            Question.id == question_id
        )
        .first()
    )

    if not question:
        raise ValueError(
            "Question not found"
        )

    existing_answer = (
        db.query(SubmissionAnswer)
        .filter(
            SubmissionAnswer.submission_id == submission_id,
            SubmissionAnswer.question_id == question_id
        )
        .first()
    )

    if existing_answer:
        raise ValueError(
            "Answer already submitted for this question"
        )

    submission_answer = SubmissionAnswer(
        submission_id=submission_id,
        question_id=question_id,
        answer_text=answer_text,
        file_url=file_url,
        
    )

    db.add(submission_answer)
    db.commit()
    db.refresh(submission_answer)

    return submission_answer

def get_answers_by_submission(
    db: Session,
    submission_id: int,
    current_student_id: int
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
    if submission.student_id != current_student_id:
        raise ValueError(
            "Access denied"
    )

    answers = (
        db.query(SubmissionAnswer)
        .filter(
            SubmissionAnswer.submission_id == submission_id
        )
        .all()
    )

    return answers