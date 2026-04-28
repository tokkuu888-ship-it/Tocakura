from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Seminar(Base):
    __tablename__ = "seminars"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    window = Column(String, nullable=True)
    session_datetime = Column(DateTime, nullable=True)
    duration_minutes = Column(Integer, default=90)
    remote_link = Column(String, nullable=True)
    attendance_required = Column(Boolean, default=True)
    min_faculty_panel = Column(Integer, default=3)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    coordinator_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    moderator_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", foreign_keys=[owner_id], back_populates="seminars")
    coordinator = relationship("User", foreign_keys=[coordinator_id])
    moderator = relationship("User", foreign_keys=[moderator_id])
    progresses = relationship("Progress", back_populates="seminar")
