from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    role: Optional[str] = "student"


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
