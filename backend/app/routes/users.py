from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
def list_users():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="List users endpoint not implemented")
