# utils/session_utils.py
from sqlalchemy.orm import sessionmaker
from db import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Creates and returns a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def close_session(db):
    """Closes the database session."""
    db.close()