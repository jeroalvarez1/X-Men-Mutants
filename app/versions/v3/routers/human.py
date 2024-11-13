from ..schemes.human import HumanCreate
from ..services import human as human_service
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/mutant/", response_model=bool)
def mutant(human: HumanCreate):
    try:
        is_mutant = human_service.is_mutant(human.dna)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if is_mutant:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Mutant detected"})
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

@router.get("/stats/", response_model=dict)
def stats():
    try:
        stats = human_service.stats()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return stats