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
from app.api import submission_answer

from app.api.evaluation import (
    router as evaluation_router
)
from app.api.review import (
    router as review_router
)
from app.api.result import (
    router as result_router
)
from app.api.analytics import (
    router as analytics_router
)
from app.api.dashboard import (
    router as dashboard_router
)
from app.api.organization_dashboard import (
    router as organization_dashboard_router
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
app.include_router(submission_answer.router)
app.include_router(evaluation_router)
app.include_router(review_router)
app.include_router(result_router)
app.include_router(analytics_router)
app.include_router(dashboard_router)
app.include_router(organization_dashboard_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to InsightED API"
    }

