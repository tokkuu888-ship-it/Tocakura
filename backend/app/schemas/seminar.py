from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class SeminarBase(BaseModel):
    title: str
    description: Optional[str] = None
    window: Optional[str] = None
    session_datetime: Optional[datetime] = None
    duration_minutes: Optional[int] = 90
    remote_link: Optional[str] = None
    attendance_required: Optional[bool] = True
    min_faculty_panel: Optional[int] = 3
    coordinator_id: Optional[int] = None
    moderator_id: Optional[int] = None


class SeminarCreate(SeminarBase):
    owner_id: int


class SeminarRead(SeminarBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
