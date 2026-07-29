from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.database.base import Base
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    roll_number = Column(
        String,
        unique=True,
        nullable=False
    )

    class_name = Column(
        String,
        nullable=False
    )

    section = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    user = relationship(
    "User",
    back_populates="student"
    )

    organization = relationship(
    "Organization",
    back_populates="students"
    )
    
    classrooms = relationship(
    "ClassroomStudent",
    back_populates="student"
    )
    
    submissions = relationship(
    "Submission",
    back_populates="student"
    )