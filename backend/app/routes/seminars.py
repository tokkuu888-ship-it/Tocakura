from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.seminar import SeminarCreate, SeminarRead

router = APIRouter(prefix="/seminars", tags=["seminars"])


@router.get("/", response_model=List[SeminarRead])
def list_seminars():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="List seminars endpoint not implemented")


@router.post("/", response_model=SeminarRead, status_code=status.HTTP_201_CREATED)
def create_seminar(seminar: SeminarCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Create seminar endpoint not implemented")
