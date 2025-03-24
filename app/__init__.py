from flask import Flask
from app.config import Config
from app.core.extensions import db, migrate
from app.utils.firebase import initialize_firebase

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config first

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Firebase (after config is loaded)
    initialize_firebase()

    return app