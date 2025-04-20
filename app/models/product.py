from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date)
    location = db.Column(db.String(200))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))