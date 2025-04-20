from app import db

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donation_id = db.Column(db.Integer, db.ForeignKey('donation.id'), nullable=False)
    transporter_name = db.Column(db.String(150), nullable=False)
    vehicle_plate = db.Column(db.String(20))
    transport_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='Scheduled')  # 'Scheduled', 'In Transit', 'Completed', 'Cancelled'