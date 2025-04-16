from app import app, db, user_bp

if __name__ == '__main__':
    db.init_app(app)  # Initialize the database with the app context
    with app.app_context():
        from app.models import user
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)