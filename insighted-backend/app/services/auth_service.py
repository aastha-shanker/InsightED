from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.security import hash_password
from app.utils.security import verify_password


def register_user(
    db: Session,
    name: str,
    email: str,
    password: str,
    role: str,
    organization_id: int | None = None
):
    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        raise ValueError("User already exists")

    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        role=role,
        organization_id=organization_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
def login_user(
    db: Session,
    email: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    valid = verify_password(
        password,
        user.password_hash
    )

    if not valid:
        return None

    return user