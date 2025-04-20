from app import db, bcrypt

class User(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    username = db.Column(db.String(50), unique=True, index=True, nullable=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Admin, Donor, Recipient

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def verify_password(hashed_pw, password):
        return bcrypt.check_password_hash(hashed_pw, password)
