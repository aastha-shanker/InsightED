from pydantic import BaseModel


class QuestionCreate(BaseModel):
    assessment_id: int
    question_text: str
    question_type: str
    marks: int


class QuestionResponse(BaseModel):
    id: int
    assessment_id: int
    question_text: str
    question_type: str
    marks: int

    class Config:
        from_attributes = True