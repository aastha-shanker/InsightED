from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.analytics_schema import (
    AssessmentAnalyticsResponse
)

from app.services.analytics_service import (
    get_assessment_analytics
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get(
    "/assessment/{assessment_id}",
    response_model=AssessmentAnalyticsResponse
)
def get_assessment_analytics_endpoint(
    assessment_id: int,
    db: Session = Depends(get_db)
):

    try:

        analytics = get_assessment_analytics(
            db=db,
            assessment_id=assessment_id
        )

        return analytics

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )