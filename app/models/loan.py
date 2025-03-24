# Loan model
from app.core.extensions import db

class Loan(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    loan_amount = db.Column(db.Numeric, nullable=False)
    interest_rate = db.Column(db.Numeric, nullable=False)
    tenure_months = db.Column(db.Integer, nullable=False)
    outstanding_principal = db.Column(db.Numeric, nullable=False)
    status = db.Column(db.String, default='pending')  # pending/approved/rejected/closed
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=db.func.now())