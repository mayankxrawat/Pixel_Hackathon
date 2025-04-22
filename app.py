from flask import Flask, render_template
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.faculty import faculty_bp
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(faculty_bp)

# 404 Error Handler
@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", error="Page not found"), 404

if __name__ == "_main_":
    app.run(debug=True)
