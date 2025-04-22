from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta
from models import db, Faculty, PunchLog, Holiday
from utils import calculate_hours, get_adjusted_weekly_target
from auth import token_required

app = Flask(__name__)
CORS(app)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faculty_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)

# ---------------------------------------
# Routes
# ---------------------------------------

@app.route('/api/punch', methods=['POST'])
@token_required
def punch_time(current_user):
    action = request.json.get('action')  # "in" or "out"
    if action not in ['in', 'out']:
        return jsonify({'error': 'Invalid action'}), 400

    new_log = PunchLog(
        faculty_id=current_user.id,
        timestamp=datetime.now(),
        action=action
    )
    db.session.add(new_log)
    db.session.commit()

    return jsonify({'message': f'Punch-{action} logged successfully'}), 201

@app.route('/api/dashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    logs = PunchLog.query.filter_by(faculty_id=current_user.id).all()
    holidays = Holiday.query.all()
    total_hours, weekly_hours = calculate_hours(logs)

    required_hours = get_adjusted_weekly_target(current_user.designation, holidays)

    remaining = max(0, required_hours - weekly_hours)

    return jsonify({
        'name': current_user.name,
        'designation': current_user.designation,
        'weekly_hours': weekly_hours,
        'required_hours': required_hours,
        'remaining_hours': remaining
    })

@app.route('/api/admin/faculty/<int:faculty_id>/status', methods=['GET'])
@token_required
def faculty_status(current_user, faculty_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    faculty = Faculty.query.get(faculty_id)
    logs = PunchLog.query.filter_by(faculty_id=faculty_id).all()
    total_hours, weekly_hours = calculate_hours(logs)
    holidays = Holiday.query.all()
    required_hours = get_adjusted_weekly_target(faculty.designation, holidays)

    return jsonify({
        'faculty': faculty.name,
        'designation': faculty.designation,
        'weekly_hours': weekly_hours,
        'required_hours': required_hours
    })

# ---------------------------------------
# Initialize
# ---------------------------------------
@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)