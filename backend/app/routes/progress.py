from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.progress import ProgressCreate, ProgressRead

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/", response_model=List[ProgressRead])
def list_progress():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="List progress endpoint not implemented")


@router.post("/", response_model=ProgressRead, status_code=status.HTTP_201_CREATED)
def submit_progress(progress: ProgressCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Submit progress endpoint not implemented")
