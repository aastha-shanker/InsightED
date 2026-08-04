from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.leaderboard_schema import (
    LeaderboardEntryResponse
)

from app.services.leaderboard_service import (
    get_classroom_leaderboard
)

router = APIRouter(
    prefix="/leaderboard",
    tags=["Leaderboard"]
)


@router.get(
    "/classroom/{classroom_id}",
    response_model=list[
        LeaderboardEntryResponse
    ]
)
def get_classroom_leaderboard_endpoint(
    classroom_id: int,
    db: Session = Depends(get_db)
):

    try:

        return get_classroom_leaderboard(
            db=db,
            classroom_id=classroom_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )