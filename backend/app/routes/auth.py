from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register_user(user: UserCreate):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Register endpoint not implemented")


@router.post("/login")
def login_user():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Login endpoint not implemented")
