from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    industry: str | None = None
    description: str | None = None


class OrganizationResponse(BaseModel):
    id: int
    name: str
    industry: str | None
    description: str | None

    class Config:
        from_attributes = True