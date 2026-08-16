from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.models.teacher import Teacher
from app.models.student import Student
from app.models.classroom import Classroom
from app.models.assessment import Assessment


def get_organization_dashboard(
    db: Session,
    organization_id: int
):

    organization = (
        db.query(Organization)
        .filter(
            Organization.id == organization_id
        )
        .first()
    )

    if not organization:
        raise ValueError(
            "Organization not found"
        )

    total_teachers = (
        db.query(Teacher)
        .filter(
            Teacher.organization_id == organization_id
        )
        .count()
    )

    total_students = (
        db.query(Student)
        .filter(
            Student.organization_id == organization_id
        )
        .count()
    )

    total_classrooms = (
        db.query(Classroom)
        .filter(
            Classroom.organization_id == organization_id
        )
        .count()
    )

    classroom_ids = [
        classroom.id
        for classroom in (
            db.query(Classroom)
            .filter(
                Classroom.organization_id == organization_id
            )
            .all()
        )
    ]

    total_assessments = (
        db.query(Assessment)
        .filter(
            Assessment.classroom_id.in_(classroom_ids)
        )
        .count()
        if classroom_ids
        else 0
    )

    return {
        "total_teachers": total_teachers,
        "total_students": total_students,
        "total_classrooms": total_classrooms,
        "total_assessments": total_assessments
    }  