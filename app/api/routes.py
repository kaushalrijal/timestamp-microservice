from fastapi import APIRouter, Query

from app.services.converter import unix_to_utc, utc_to_unix

router = APIRouter()


@router.get("/to-unix")
def convert_to_unix(utc: str = Query(..., description="UTC datetime ISO")):
    return utc_to_unix(utc)


@router.get("/to-utc")
def convert_to_utc(unix: int = Query(..., description="UNIX timestamp")):
    return unix_to_utc(unix)
