from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

app = Flask(__name__, template_folder='templates', static_folder="static") # Cấu hình cho FE
app.config.from_object(Config)
CORS(app)  # Enable CORS for all routes

# Initialize the extensions with the app
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Import and register routes (API)
from app.controllers.user import user_bp
from app.controllers.product import product_bp
from app.controllers.donation import donation_bp
from app.controllers.dashboard import dashboard_bp
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(donation_bp)
app.register_blueprint(dashboard_bp)

# Import and register views (Frontend)
from app.views.auth import auth_bp
from app.views.landing import landing_bp
app.register_blueprint(auth_bp)
app.register_blueprint(landing_bp)