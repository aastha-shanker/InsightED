from sqlalchemy.orm import Session

from app.models.organization import Organization


def create_organization(
    db: Session,
    name: str,
    industry: str | None,
    description: str | None
):
    existing_org = (
        db.query(Organization)
        .filter(Organization.name == name)
        .first()
    )

    if existing_org:
        raise ValueError(
            "Organization already exists"
        )

    organization = Organization(
        name=name,
        industry=industry,
        description=description
    )

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization