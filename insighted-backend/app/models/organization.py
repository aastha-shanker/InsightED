from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.base import Base
from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False,
        unique=True
    )

    industry = Column(
        String,
        nullable=True
    )

    description = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    users = relationship(
    "User",
    back_populates="organization"
    )
    
    students = relationship(
    "Student",
    back_populates="organization"
    )
    
    teachers = relationship(
    "Teacher",
    back_populates="organization"
    )
    
    classrooms = relationship(
    "Classroom",
    back_populates="organization"
    )