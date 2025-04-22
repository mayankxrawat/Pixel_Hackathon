# routes/faculty.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .user import create_faculty, log_hours, get_total_hours
from db import get_db
from datetime import datetime
from pydantic import BaseModel

faculty_router = APIRouter()

class LogHoursRequest(BaseModel):
    date: str
    hours_worked: float

@faculty_router.post("/faculty/log_hours")
def log_faculty_hours(faculty_id: int, hours: LogHoursRequest, db: Session = Depends(get_db)):
    try:
        # Log the work hours for the faculty member
        log_hours(db, faculty_id, hours.date, hours.hours_worked)
        return {"message": "Work hours logged successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error logging work hours")

@faculty_router.get("/faculty/{faculty_id}/total_hours")
def get_faculty_hours(faculty_id: int, db: Session = Depends(get_db)):
    try:
        total_hours = get_total_hours(db, faculty_id)
        return {"faculty_id": faculty_id, "total_hours": total_hours}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving total hours")
