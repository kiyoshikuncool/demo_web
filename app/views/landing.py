from flask import render_template
from flask import Blueprint

landing_view_bp = Blueprint('landing', __name__)

@landing_view_bp.get('/')
def landing():
    return render_template('landing.html')

@landing_view_bp.get('/select-role')
def selectRole():
    return render_template('select-role.html')