from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.user import User
from app.models.organization import Organization


def create_student(
    db: Session,
    user_id: int,
    organization_id: int,
    roll_number: str,
    class_name: str,
    section: str
):
    
    # Check User Exists
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise ValueError("User not found")
    
    if user.role != "student":
      raise ValueError(
        "Only users with student role can create student profiles"
      ) 
    
    if user.teacher:
      raise ValueError(
        "Teacher cannot have a student profile"
      )

    # Check Organization Exists
    organization = (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )

    if not organization:
        raise ValueError("Organization not found")

    # Check Roll Number Unique
    existing_roll = (
        db.query(Student)
        .filter(Student.roll_number == roll_number)
        .first()
    )

    if existing_roll:
        raise ValueError("Roll number already exists")

    # Check Student Profile Doesn't Exist
    existing_student = (
        db.query(Student)
        .filter(Student.user_id == user_id)
        .first()
    )

    if existing_student:
        raise ValueError(
            "Student profile already exists for this user"
        )

    # Create Student
    student = Student(
        user_id=user_id,
        organization_id=organization_id,
        roll_number=roll_number,
        class_name=class_name,
        section=section
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student