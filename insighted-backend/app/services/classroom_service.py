import random
import string

from sqlalchemy.orm import Session

from app.models.classroom import Classroom
from app.models.classroom_student import ClassroomStudent
from app.models.teacher import Teacher
from app.models.student import Student
from app.models.organization import Organization


def generate_join_code(length=6):
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=length
        )
    )


def create_classroom(
    db: Session,
    teacher_id: int,
    organization_id: int,
    name: str
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

    existing_classroom = (
        db.query(Classroom)
        .filter(
            Classroom.teacher_id == teacher_id,
            Classroom.name == name
        )
        .first()
    )

    if existing_classroom:
        raise ValueError(
            "Classroom already exists"
        )

    join_code = generate_join_code()

    while (
        db.query(Classroom)
        .filter(
            Classroom.join_code == join_code
        )
        .first()
    ):
        join_code = generate_join_code()

    classroom = Classroom(
        teacher_id=teacher_id,
        organization_id=organization_id,
        name=name,
        join_code=join_code
    )

    db.add(classroom)
    db.commit()
    db.refresh(classroom)

    return classroom
def join_classroom(
    db: Session,
    student_id: int,
    join_code: str
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

    classroom = (
        db.query(Classroom)
        .filter(
            Classroom.join_code == join_code
        )
        .first()
    )

    if not classroom:
        raise ValueError(
            "Invalid join code"
        )

    existing = (
        db.query(ClassroomStudent)
        .filter(
            ClassroomStudent.classroom_id == classroom.id,
            ClassroomStudent.student_id == student_id
        )
        .first()
    )

    if existing:
        raise ValueError(
            "Student already enrolled"
        )

    enrollment = ClassroomStudent(
        classroom_id=classroom.id,
        student_id=student_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment
  
def get_student_classrooms(
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

    classrooms = (
        db.query(Classroom)
        .join(
            ClassroomStudent,
            Classroom.id == ClassroomStudent.classroom_id
        )
        .filter(
            ClassroomStudent.student_id == student_id
        )
        .all()
    )

    return classrooms