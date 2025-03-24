# Transaction model
from app.core.extensions import db

class Transaction(db.Model):
    txn_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.loan_id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    type = db.Column(db.String, nullable=False)  # emi/full/custom/cash
    status = db.Column(db.String, nullable=False)  # success/failed/pending
    gateway_txn_id = db.Column(db.String)
    gateway_response = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime, default=db.func.now())