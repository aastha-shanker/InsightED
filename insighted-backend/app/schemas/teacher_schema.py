from pydantic import BaseModel


class TeacherCreate(BaseModel):
    user_id: int
    organization_id: int
    employee_id: str
    department: str
    designation: str


class TeacherResponse(BaseModel):
    id: int
    user_id: int
    organization_id: int
    employee_id: str
    department: str
    designation: str

    class Config:
        from_attributes = True