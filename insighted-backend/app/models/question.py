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


class Question(Base):
    __tablename__ = "questions"

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

    question_text = Column(
        String,
        nullable=False
    )

    question_type = Column(
        String,
        nullable=False
    )

    marks = Column(
        Integer,
        nullable=False
    )
    
    option_a = Column(
    String,
    nullable=True
    )

    option_b = Column(
    String,
    nullable=True
    )

    option_c = Column(
    String,
    nullable=True
    )

    option_d = Column(
    String,
    nullable=True
    )

    correct_answer = Column(
    String,
    nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    assessment = relationship(
        "Assessment",
        back_populates="questions"
    )