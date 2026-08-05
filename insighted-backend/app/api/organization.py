from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.organization_schema import (
    OrganizationCreate,
    OrganizationResponse
)

from app.services.organization_service import (
    create_organization
)
from app.dependencies.roles import (
    get_current_super_admin
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)
@router.post(
    "",
    response_model=OrganizationResponse
)
def create_org(
    request: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(
        get_current_super_admin
    )
):
    try:
        return create_organization(
            db=db,
            name=request.name,
            industry=request.industry,
            description=request.description
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )