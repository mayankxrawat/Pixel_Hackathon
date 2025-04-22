# routes/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .user import get_all_faculty_hours
from db import get_db

admin_router = APIRouter()

@admin_router.get("/admin/faculty_summary")
def faculty_summary(db: Session = Depends(get_db)):
    try:
        summary = get_all_faculty_hours(db)
        return {"faculty_summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving summary")