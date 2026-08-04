from pydantic import BaseModel


class LeaderboardEntryResponse(BaseModel):
    rank: int
    student_id: int
    student_name: str
    average_score: float