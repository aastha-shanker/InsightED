from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String, nullable=False)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=True
    )

    organization = relationship(
        "Organization",
        back_populates="users"
    )
    
    student = relationship(
    "Student",
    back_populates="user",
    uselist=False
    )
    
    teacher = relationship(
    "Teacher",
    back_populates="user",
    uselist=False
    )