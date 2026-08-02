from pydantic import BaseModel


class ReviewCreate(BaseModel):
    marks_obtained: int
    feedback: str | None = None