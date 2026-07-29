from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    submitted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    status = Column(
        String,
        nullable=False,
        default="submitted"
    )

    total_score = Column(
        Integer,
        nullable=True
    )

    assessment = relationship(
        "Assessment",
        back_populates="submissions"
    )

    student = relationship(
        "Student",
        back_populates="submissions"
    )