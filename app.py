from app import app, db

if __name__ == '__main__':
    with app.app_context():
        from app.models import user
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)