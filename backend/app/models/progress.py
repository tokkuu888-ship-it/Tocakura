from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Progress(Base):
    __tablename__ = "progresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seminar_id = Column(Integer, ForeignKey("seminars.id"), nullable=False)
    progress_percent = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    report_summary = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)

    user = relationship("User", back_populates="progresses")
    seminar = relationship("Seminar", back_populates="progresses")
