from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.models.classroom import Classroom
from app.models.assessment import Assessment
from app.models.submission import Submission
from app.models.student import Student
from app.models.classroom_student import ClassroomStudent


def get_teacher_dashboard(
    db: Session,
    teacher_id: int
):

    teacher = (
        db.query(Teacher)
        .filter(
            Teacher.id == teacher_id
        )
        .first()
    )

    if not teacher:
        raise ValueError(
            "Teacher not found"
        )

    classrooms = (
        db.query(Classroom)
        .filter(
            Classroom.teacher_id == teacher_id
        )
        .all()
    )

    total_classrooms = len(
        classrooms
    )

    classroom_ids = [
        classroom.id
        for classroom in classrooms
    ]

    if not classroom_ids:

        return {
            "total_classrooms": 0,
            "total_assessments": 0,
            "total_students": 0,
            "total_submissions": 0
        }

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.classroom_id.in_(
                classroom_ids
            )
        )
        .all()
    )

    total_assessments = len(
        assessments
    )

    assessment_ids = [
        assessment.id
        for assessment in assessments
    ]

    if not assessment_ids:

        return {
            "total_classrooms": total_classrooms,
            "total_assessments": 0,
            "total_students": 0,
            "total_submissions": 0
        }

    submissions = (
        db.query(Submission)
        .filter(
            Submission.assessment_id.in_(
                assessment_ids
            )
        )
        .all()
    )

    total_submissions = len(
        submissions
    )

    student_ids = set()

    for submission in submissions:

        student_ids.add(
            submission.student_id
        )

    total_students = len(
        student_ids
    )
    

    return {
        "total_classrooms": total_classrooms,
        "total_assessments": total_assessments,
        "total_students": total_students,
        "total_submissions": total_submissions
    }
    
def get_student_dashboard(
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

    classroom_memberships = (
        db.query(ClassroomStudent)
        .filter(
            ClassroomStudent.student_id == student_id
        )
        .all()
    )

    total_classrooms = len(
        classroom_memberships
    )

    classroom_ids = [
        membership.classroom_id
        for membership in classroom_memberships
    ]

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.classroom_id.in_(
                classroom_ids
            )
        )
        .all()
    ) if classroom_ids else []

    total_assessments = len(
        assessments
    )

    submissions = (
        db.query(Submission)
        .filter(
            Submission.student_id == student_id
        )
        .all()
    )

    completed_assessments = len(
        submissions
    )
    pending_assessments = (
    total_assessments -
    completed_assessments
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

    return {
    "student_id": student_id,
    "joined_classrooms": total_classrooms,
    "pending_assessments": pending_assessments,
    "completed_assessments": completed_assessments,
    "average_score": average_score
  }