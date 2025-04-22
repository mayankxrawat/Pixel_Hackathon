# routes/common.py
from fastapi import APIRouter

common_router = APIRouter()

@common_router.get("/status")
def check_status():
    return {"status": "Faculty Work Hours Tracker is up and running!"}