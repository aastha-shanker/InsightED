from pydantic import BaseModel


class ClassroomCreate(BaseModel):
    teacher_id: int
    organization_id: int
    name: str


class ClassroomResponse(BaseModel):
    id: int
    teacher_id: int
    organization_id: int
    name: str
    join_code: str

    class Config:
        from_attributes = True


class JoinClassroomRequest(BaseModel):
    student_id: int
    join_code: str
class ClassroomListResponse(BaseModel):
    id: int
    name: str
    join_code: str

    class Config:
        from_attributes = True