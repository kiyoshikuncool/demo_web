from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config

app = Flask(__name__, template_folder='../templates', static_folder="../static") # Cấu hình cho FE
app.config.from_object(Config)

db = SQLAlchemy()
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Initialize the database with the app context
db.init_app(app) 
with app.app_context():
    from app.models import user
    db.create_all()  # Create tables if they don't exist

# Route của FE
@app.get('/')
@app.get('/index')
def index():
    return render_template('index.html')

@app.get('/signup')
def signup():
    return render_template('register.html')

@app.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Import and register routes (API)
from app.controllers.user import user_bp
app.register_blueprint(user_bp)