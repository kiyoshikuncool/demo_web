from flask import render_template
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.get('/')
@auth_bp.get('/index')
def index():
    return render_template('index.html')

@auth_bp.get('/signup')
def signup():
    return render_template('register.html')

@auth_bp.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')