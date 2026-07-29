from pydantic import BaseModel


class SubmissionAnswerCreate(BaseModel):
    submission_id: int
    question_id: int
    answer_text: str | None = None
    file_url: str | None = None


class SubmissionAnswerResponse(BaseModel):
    id: int
    submission_id: int
    question_id: int
    answer_text: str | None
    file_url: str | None
    marks_obtained: int | None

    class Config:
        from_attributes = True