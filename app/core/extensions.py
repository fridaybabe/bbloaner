# Flask-SQLAlchemy, Flask-Migrate etc.
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions here (they'll be tied to the app later)
db = SQLAlchemy()
migrate = Migrate()