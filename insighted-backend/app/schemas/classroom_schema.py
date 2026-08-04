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
        
class ClassroomDetailResponse(BaseModel):
    id: int
    name: str
    join_code: str
    teacher_id: int
    total_students: int
    total_assessments: int
    
class ClassroomStudentResponse(BaseModel):
    id: int
    name: str
    email: str


class ClassroomStudentsResponse(BaseModel):
    students: list[ClassroomStudentResponse]

class AssessmentResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True