# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .models import Base

DATABASE_URL = "sqlite:///./faculty_work_hours.db"  # Change this to your preferred database

# Create SQLAlchemy engine and session maker
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Create all tables in the database
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {e}")
