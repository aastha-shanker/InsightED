from sqlalchemy.orm import Session

from app.models.assessment import Assessment
from app.models.submission import Submission


def get_assessment_analytics(
    db: Session,
    assessment_id: int,
    current_teacher_id: int
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
    
    if assessment.classroom.teacher_id != current_teacher_id:
        raise ValueError(
            "Access denied"
        )

    submissions = (
        db.query(Submission)
        .filter(
            Submission.assessment_id == assessment_id
        )
        .all()
    )

    total_submissions = len(submissions)

    evaluated_submissions = len(
        [
            submission
            for submission in submissions
            if submission.status == "evaluated"
        ]
    )

    scores = [
        submission.total_score
        for submission in submissions
        if submission.total_score is not None
    ]

    if not scores:

        return {
            "assessment_id": assessment_id,
            "total_submissions": total_submissions,
            "evaluated_submissions": evaluated_submissions,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0
        }

    return {
        "assessment_id": assessment_id,
        "total_submissions": total_submissions,
        "evaluated_submissions": evaluated_submissions,
        "average_score": sum(scores) / len(scores),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }