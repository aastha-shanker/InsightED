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


class Assessment(Base):
    __tablename__ = "assessments"

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

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    assessment_type = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    classroom = relationship(
    "Classroom",
    back_populates="assessments"
    )
    
    total_marks = Column(
    Integer,
    nullable=False
    )
    
    due_date = Column(
    DateTime(timezone=True),
    nullable=True
    )
    
    questions = relationship(
    "Question",
    back_populates="assessment"
    )
    
    submissions = relationship(
    "Submission",
    back_populates="assessment"
    )
   
    