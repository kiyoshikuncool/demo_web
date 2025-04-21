from flask import render_template
from flask import Blueprint

auth_view_bp = Blueprint('auth', __name__)

@auth_view_bp.get('/login')
def index():
    return render_template('login.html')

@auth_view_bp.get('/signup')
def signup():
    return render_template('register.html')

@auth_view_bp.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')