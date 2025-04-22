from datetime import datetime, timedelta
from models import Holiday

# Helper: returns start of the current week (Monday)
def get_week_start():
    today = datetime.now().date()
    start = today - timedelta(days=today.weekday())  # Monday
    return start

# Calculate total work hours from logs
def calculate_hours(logs):
    logs = sorted(logs, key=lambda x: x.timestamp)
    total_minutes = 0
    weekly_minutes = 0
    week_start = get_week_start()

    punch_in_time = None
    for log in logs:
        if log.action == 'in':
            punch_in_time = log.timestamp
        elif log.action == 'out' and punch_in_time:
            duration = log.timestamp - punch_in_time
            minutes = int(duration.total_seconds() / 60)
            total_minutes += minutes
            if punch_in_time.date() >= week_start:
                weekly_minutes += minutes
            punch_in_time = None  # reset after matching pair

    return round(total_minutes / 60, 2), round(weekly_minutes / 60, 2)  # hours

# Get adjusted weekly target
def get_adjusted_weekly_target(designation, holidays):
    base_hours = {
        'Assistant Professor': 35,
        'Professor': 30
    }.get(designation, 30)  # default for "Others"

    week_start = get_week_start()
    week_end = week_start + timedelta(days=6)

    # Count holidays in current week
    week_holidays = [
        h.date for h in holidays
        if week_start <= h.date <= week_end or h.date.weekday() == 6  # Sunday
    ]
    working_days = 7 - len(week_holidays)

    adjusted_hours = (base_hours / 5) * working_days
    return round(adjusted_hours, 2)
