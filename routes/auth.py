# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .user import create_faculty
from db import get_db
from pydantic import BaseModel

auth_router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

# Dummy login - replace with real logic
@auth_router.post("/login")
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    # Logic to authenticate the user goes here (e.g., check email and password)
    faculty = db.query(Faculty).filter(Faculty.email == credentials.email).first()
    if not faculty:  # If no such faculty exists
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Faculty not found")
    # Return a token or successful login response
    return {"message": f"Welcome, {faculty.name}"}
