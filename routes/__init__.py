# routes/_init_.py
from fastapi import FastAPI
from flask import Flask
from .auth import auth_router
from .admin import admin_router
from .faculty import faculty_router
from .common import common_router

def register_routes(app):
    # Register all the routes to the FastAPI app or Flask app
    app.include_router(auth_router)
    app.include_router(admin_router)
    app.include_router(faculty_router)
    app.include_router(common_router)