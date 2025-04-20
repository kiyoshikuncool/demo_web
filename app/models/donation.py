from app import db
from datetime import datetime

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quantity = db.Column(db.Integer, nullable=False)
    donated_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Pending')  # 'Pending', 'Accepted', 'Rejected'