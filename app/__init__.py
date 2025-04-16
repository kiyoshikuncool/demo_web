from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config

app = Flask(__name__, template_folder='../templates', static_folder="../static") # Cấu hình cho FE
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

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