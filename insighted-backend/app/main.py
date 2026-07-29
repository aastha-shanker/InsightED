from fastapi import FastAPI

from app.api.auth import router as auth_router

from app.database.connection import engine
from app.database.base import Base

# Import models so SQLAlchemy registers them
import app.models

from app.api.organization import (
    router as organization_router
)

from app.api.student import (
    router as student_router
)
from app.api.teacher import (
    router as teacher_router
)
from app.api.assessment import (
    router as assessment_router
)
from app.api.classroom import (
    router as classroom_router
)
from app.api.question import (
    router as question_router
)
from app.api.submission import (
    router as submission_router
)


app = FastAPI(title="InsightED API")



app.include_router(auth_router)
app.include_router(organization_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(assessment_router)
app.include_router(classroom_router)
app.include_router(question_router)
app.include_router(submission_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to InsightED API"
    }

