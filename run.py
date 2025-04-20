from app import app, db

# Import models theo thứ tự để tạo bảng đúng thứ tự
from app.models.organization import Organization
from app.models.product import Product
from app.models.user import User
from app.models.donation import Donation

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=False)