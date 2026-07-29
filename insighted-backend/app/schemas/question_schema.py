from pydantic import BaseModel
from pydantic import BaseModel

class QuestionCreate(BaseModel):
    assessment_id: int
    question_text: str
    question_type: str
    marks: int

    option_a: str | None = None
    option_b: str | None = None
    option_c: str | None = None
    option_d: str | None = None

    correct_answer: str | None = None

class QuestionResponse(BaseModel):
    id: int
    assessment_id: int
    question_text: str
    question_type: str
    marks: int

    option_a: str | None
    option_b: str | None
    option_c: str | None
    option_d: str | None

    correct_answer: str | None

    class Config:
        from_attributes = True