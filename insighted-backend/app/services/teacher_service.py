from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.models.user import User
from app.models.organization import Organization


def create_teacher(
    db: Session,
    user_id: int,
    organization_id: int,
    employee_id: str,
    department: str,
    designation: str
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise ValueError("User not found")
    
    if user.role != "teacher":
      raise ValueError(
        "Only users with teacher role can create teacher profiles"
      )
    
    if user.student:
      raise ValueError(
        "Student cannot have a teacher profile"
      )

    organization = (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )

    if not organization:
        raise ValueError("Organization not found")

    existing_employee = (
        db.query(Teacher)
        .filter(Teacher.employee_id == employee_id)
        .first()
    )

    if existing_employee:
        raise ValueError(
            "Employee ID already exists"
        )

    existing_teacher = (
        db.query(Teacher)
        .filter(Teacher.user_id == user_id)
        .first()
    )

    if existing_teacher:
        raise ValueError(
            "Teacher profile already exists for this user"
        )

    teacher = Teacher(
        user_id=user_id,
        organization_id=organization_id,
        employee_id=employee_id,
        department=department,
        designation=designation
    )

    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    return teacher