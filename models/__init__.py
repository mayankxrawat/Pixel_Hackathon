# faculty_tracker/_init_.py

print("Faculty Work Hours Tracker package initialized")

from .db import init_db, get_connection
from .tracker import log_hours, get_hours_summary
from .models import Faculty, WorkLog

_all_ = [
    'init_db',
    'get_connection',
    'log_hours',
    'get_hours_summary',
    'Faculty',
    'WorkLog'
]