# user.py
from sqlalchemy.orm import Session
from .models import Faculty, WorkLog
from datetime import datetime

# Create a new faculty member
def create_faculty(db: Session, name: str, email: str):
    db_faculty = Faculty(name=name, email=email)
    db.add(db_faculty)
    db.commit()
    db.refresh(db_faculty)
    return db_faculty

# Log work hours for a faculty member
def log_hours(db: Session, faculty_id: int, date: str, hours_worked: float):
    db_worklog = WorkLog(faculty_id=faculty_id, date=date, hours_worked=hours_worked)
    db.add(db_worklog)
    db.commit()
    db.refresh(db_worklog)
    return db_worklog

# Get faculty details
def get_faculty(db: Session, faculty_id: int):
    return db.query(Faculty).filter(Faculty.id == faculty_id).first()

# Get all work logs for a faculty member
def get_work_logs(db: Session, faculty_id: int):
    return db.query(WorkLog).filter(WorkLog.faculty_id == faculty_id).all()

# Get the total hours worked by a faculty member
def get_total_hours(db: Session, faculty_id: int):
    work_logs = get_work_logs(db, faculty_id)
    total_hours = sum(log.hours_worked for log in work_logs)
    return total_hours

# Get a summary of all work hours for all faculty members
def get_all_faculty_hours(db: Session):
    faculty_list = db.query(Faculty).all()
    summary = {}
    for faculty in faculty_list:
        total_hours = get_total_hours(db, faculty.id)
        summary[faculty.name] = total_hours
    return summary
