from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.result_schema import (
    ResultResponse
)

from app.services.result_service import (
    get_result_by_submission,
    get_results_by_student
)

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)

@router.get(
    "/submission/{submission_id}",
    response_model=ResultResponse
)
def get_result_by_submission_endpoint(
    submission_id: int,
    db: Session = Depends(get_db)
):

    try:

        result = get_result_by_submission(
            db=db,
            submission_id=submission_id
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
        
@router.get(
    "/student/{student_id}",
    response_model=list[ResultResponse]
)
def get_results_by_student_endpoint(
    student_id: int,
    db: Session = Depends(get_db)
):

    try:

        results = get_results_by_student(
            db=db,
            student_id=student_id
        )

        return results

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )