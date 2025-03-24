# User model
from app.core.extensions import db

class User(db.Model):
    user_id = db.Column(db.String, primary_key=True)  # Firebase UID
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())