
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Faculty(Base):
    _tablename_ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    work_logs = relationship("WorkLog", back_populates="faculty")

class WorkLog(Base):
    _tablename_ = "work_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)  # Ideally use Date type
    hours_worked = Column(Float)
    faculty_id = Column(Integer, ForeignKey("faculty.id"))

    faculty = relationship("Faculty", back_populates="work_logs")