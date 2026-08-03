from pydantic import BaseModel


class TeacherDashboardResponse(BaseModel):
    total_classrooms: int
    total_assessments: int
    total_students: int
    total_submissions: int

class StudentDashboardResponse(BaseModel):
    student_id: int
    joined_classrooms: int
    pending_assessments: int
    completed_assessments: int
    average_score: float