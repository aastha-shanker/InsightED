from pydantic import BaseModel
from datetime import datetime


class SubmissionCreate(BaseModel):
    assessment_id: int
    student_id: int


class SubmissionResponse(BaseModel):
    id: int
    assessment_id: int
    student_id: int
    submitted_at: datetime
    status: str
    total_score: int | None

    class Config:
        from_attributes = True