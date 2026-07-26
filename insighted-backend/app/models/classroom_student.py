from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base
from sqlalchemy import UniqueConstraint


class ClassroomStudent(Base):
    __tablename__ = "classroom_students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    classroom_id = Column(
        Integer,
        ForeignKey("classrooms.id"),
        nullable=False
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    classroom = relationship(
        "Classroom",
        back_populates="students"
    )

    student = relationship(
        "Student",
        back_populates="classrooms"
    )
    
    __table_args__ = (
    UniqueConstraint(
        "classroom_id",
        "student_id",
        name="uq_classroom_student"
      ),
    )