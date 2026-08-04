from sqlalchemy.orm import Session

from app.models.classroom import Classroom
from app.models.classroom_student import ClassroomStudent
from app.models.student import Student
from app.models.user import User
from app.models.assessment import Assessment
from app.models.submission import Submission


def get_classroom_leaderboard(
    db: Session,
    classroom_id: int
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

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.classroom_id == classroom_id
        )
        .all()
    )

    assessment_ids = [
        assessment.id
        for assessment in assessments
    ]

    memberships = (
        db.query(ClassroomStudent)
        .filter(
            ClassroomStudent.classroom_id == classroom_id
        )
        .all()
    )

    leaderboard = []

    for membership in memberships:

        student = (
            db.query(Student)
            .filter(
                Student.id == membership.student_id
            )
            .first()
        )

        user = (
            db.query(User)
            .filter(
                User.id == student.user_id
            )
            .first()
        )

        submissions = (
            db.query(Submission)
            .filter(
                Submission.student_id == student.id,
                Submission.assessment_id.in_(assessment_ids)
            )
            .all()
        )

        scores = [
            submission.total_score
            for submission in submissions
            if submission.total_score is not None
        ]

        average_score = (
            sum(scores) / len(scores)
            if scores
            else 0
        )

        leaderboard.append(
            {
                "student_id": student.id,
                "student_name": user.name,
                "average_score": average_score
            }
        )

    leaderboard.sort(
        key=lambda x: x["average_score"],
        reverse=True
    )

    ranked_leaderboard = []

    for index, entry in enumerate(
        leaderboard,
        start=1
    ):

        ranked_leaderboard.append(
            {
                "rank": index,
                **entry
            }
        )

    return ranked_leaderboard