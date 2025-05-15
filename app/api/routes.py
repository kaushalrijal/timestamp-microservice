from fastapi import APIRouter, HTTPException, Query

from app.services.converter import unix_to_both, utc_to_both

router = APIRouter()


@router.get("/to-unix")
def convert_to_unix(utc: str = Query(...)):
    try:
        return utc_to_both(utc)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/to-utc")
def convert_to_utc(unix: int = Query(...)):
    try:
        return unix_to_both(unix)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
