# utils/time_utils.py
from datetime import datetime

def calculate_working_hours(start_time: str, end_time: str) -> float:
    """Calculates the hours worked based on start and end times."""
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    delta = end - start
    return delta.total_seconds() / 3600  # Convert seconds to hours

def format_time(hours: float) -> str:
    """Formats the working hours into a human-readable string."""
    return f"{hours:.2f} hours"