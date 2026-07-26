from pydantic import BaseModel


class StudentCreate(BaseModel):
    user_id: int
    organization_id: int
    roll_number: str
    class_name: str
    section: str


class StudentResponse(BaseModel):
    id: int
    user_id: int
    organization_id: int
    roll_number: str
    class_name: str
    section: str

    class Config:
        from_attributes = True