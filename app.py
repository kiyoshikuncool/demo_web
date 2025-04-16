from app import app, db

with app.app_context():
    db.create_all()  # Create tables if they don't exist
    db.session.commit() # Commit the changes to database
app.run(debug=True)