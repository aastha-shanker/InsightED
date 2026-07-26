from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    UniqueConstraint
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    teacher_id = Column(
        Integer,
        ForeignKey("teachers.id"),
        nullable=False
    )

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )

    join_code = Column(
        String,
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    teacher = relationship(
        "Teacher",
        back_populates="classrooms"
    )

    organization = relationship(
        "Organization",
        back_populates="classrooms"
    )

    students = relationship(
        "ClassroomStudent",
        back_populates="classroom"
    )
    assessments = relationship(
    "Assessment",
    back_populates="classroom"
    )
    
    __table_args__ = (
    UniqueConstraint(
        "teacher_id",
        "name",
        name="uq_teacher_classroom"
      ),
    )