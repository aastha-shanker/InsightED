from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.organization_dashboard_schema import (
    OrganizationDashboardResponse
)

from app.services.organization_dashboard_service import (
    get_organization_dashboard
)

router = APIRouter(
    prefix="/organization-dashboard",
    tags=["Organization Dashboard"]
)


@router.get(
    "/{organization_id}",
    response_model=OrganizationDashboardResponse
)
def get_organization_dashboard_endpoint(
    organization_id: int,
    db: Session = Depends(get_db)
):

    try:

        dashboard = get_organization_dashboard(
            db=db,
            organization_id=organization_id
        )

        return dashboard

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )