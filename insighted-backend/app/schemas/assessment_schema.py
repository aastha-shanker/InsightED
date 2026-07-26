from datetime import datetime

from pydantic import BaseModel


class AssessmentCreate(BaseModel):
    classroom_id: int
    title: str
    description: str | None = None
    assessment_type: str
    total_marks: int
    due_date: datetime | None = None


class AssessmentResponse(BaseModel):
    id: int
    classroom_id: int
    title: str
    description: str | None
    assessment_type: str
    total_marks: int
    due_date: datetime | None

    class Config:
        from_attributes = True