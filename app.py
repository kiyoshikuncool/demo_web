from app import app, db
from app.models import user

with app.app_context():
    db.create_all()  # Create tables if they don't exist
    db.session.commit() # Commit the changes to database
app.run(debug=True)