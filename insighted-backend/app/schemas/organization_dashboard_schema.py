from pydantic import BaseModel


class OrganizationDashboardResponse(BaseModel):
    total_teachers: int
    total_students: int
    total_classrooms: int
    total_assessments: int