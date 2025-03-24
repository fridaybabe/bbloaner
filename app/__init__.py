from flask import Flask
from app.config import Config
from app.core.extensions import db, migrate
from app.utils.firebase import initialize_firebase

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Firebase
    initialize_firebase()

    return app