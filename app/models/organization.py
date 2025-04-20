from app import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(300))
    description = db.Column(db.Text)
    type = db.Column(db.String(100))  # 'Supermarket', 'Startup', 'Charity'