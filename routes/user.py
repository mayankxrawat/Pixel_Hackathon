# routes/user.py
from flask import Blueprint, render_template, request, redirect, url_for

# Created a blueprint for user-related routes
user_bp = Blueprint('user', __name__)

# Route for the login page
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here, you would typically verify the username and password
        # For now, we will just redirect to the dashboard after form submission
        return redirect(url_for('user.dashboard'))
    return render_template('login.html')

# Route for the registration page
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here, you would typically save the user to the database
        # For now, we will just redirect to the login page after registration
        return redirect(url_for('user.login'))
    return render_template('register.html')

# Route for the user dashboard
@user_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route to log out (just for demonstration)
@user_bp.route('/logout')
def logout():
    # Here you would clear the user session
    return redirect(url_for('user.login'))
@user_bp.route('/create_faculty', methods=['GET', 'POST'])
def create_faculty():
    if request.method == 'POST':
        faculty_name = request.form['faculty_name']
        faculty_email = request.form['faculty_email']
        # Here, you would typically save the faculty to the database
        # For now, we will just redirect to the dashboard after form submission
        return redirect(url_for('user.dashboard'))
    return render_template('create_faculty.html')

@user_bp.route('/faculty_dashboard')
def faculty_dashboard():
    return render_template('faculty_dashboard.html')