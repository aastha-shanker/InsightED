from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    DateTime
)

from sqlalchemy.orm import relationship

from app.database.base import Base


class SubmissionAnswer(Base):
    __tablename__ = "submission_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    submission_id = Column(
        Integer,
        ForeignKey("submissions.id"),
        nullable=False
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False
    )

    answer_text = Column(
        Text,
        nullable=True
    )

    file_url = Column(
        String,
        nullable=True
    )

    marks_obtained = Column(
        Integer,
        nullable=True
    )
    
    feedback = Column(
      String,
      nullable=True
    )

    evaluated_at = Column(
      DateTime(timezone=True),
      nullable=True
    ) 

    submission = relationship(
        "Submission",
        back_populates="answers"
    )

    question = relationship(
        "Question"
    )