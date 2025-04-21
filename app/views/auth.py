from flask import render_template
from flask import Blueprint

auth_view_bp = Blueprint('auth', __name__)

@auth_view_bp.get('/login')
def index():
    return render_template('auth/login.html')

@auth_view_bp.get('/register')
def signup():
    return render_template('auth/register.html')

@auth_view_bp.get('/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')