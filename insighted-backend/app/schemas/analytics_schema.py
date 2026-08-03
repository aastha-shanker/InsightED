from pydantic import BaseModel


class AssessmentAnalyticsResponse(BaseModel):
    assessment_id: int
    total_submissions: int
    evaluated_submissions: int
    average_score: float
    highest_score: int
    lowest_score: int