from pydantic import BaseModel
from typing import Optional


class ProgressBase(BaseModel):
    user_id: int
    seminar_id: int
    progress_percent: int = 0
    completed: bool = False
    report_summary: Optional[str] = None
    feedback: Optional[str] = None


class ProgressCreate(ProgressBase):
    pass


class ProgressRead(ProgressBase):
    id: int

    class Config:
        orm_mode = True
