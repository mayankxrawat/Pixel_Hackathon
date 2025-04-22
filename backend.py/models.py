from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Faculty(db.Model):
    _tablename_ = 'faculties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    logs = db.relationship('PunchLog', backref='faculty', lazy=True)

class PunchLog(db.Model):
    _tablename_ = 'punch_logs'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    action = db.Column(db.String(10), nullable=False)  # 'in' or 'out'

class Holiday(db.Model):
    _tablename_ = 'holidays'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    name = db.Column(db.String(100))