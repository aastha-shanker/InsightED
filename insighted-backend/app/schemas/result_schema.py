from pydantic import BaseModel


class ResultResponse(BaseModel):
    id: int
    assessment_id: int
    student_id: int
    status: str
    total_score: int | None

    class Config:
        from_attributes = True
    class Config:
        from_attributes = True