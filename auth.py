from functools import wraps
from flask import request, jsonify
from models import Faculty
from models import db

# Dummy in-memory token map for demo (Replace with JWT in production)
fake_tokens = {
    "demo-token-1": "admin@gehu.edu",
    "demo-token-2": "professor@gehu.edu",
    "demo-token-3": "assistant@gehu.edu"
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token or token not in fake_tokens:
            return jsonify({'error': 'Unauthorized or missing token'}), 401

        email = fake_tokens[token]
        user = Faculty.query.filter_by(email=email).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return f(user, *args, **kwargs)

    return decorated

