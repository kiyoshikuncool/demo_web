from app import app, db
from app.models import user

if __name__ == '__main__':
    with app.app_context():
        from app.models import user
        db.create_all()  # Create tables if they don't exist
        db.session.commit() # Commit the changes to database
    app.run(debug=True)