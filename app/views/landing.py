from flask import render_template
from flask import Blueprint

landing_bp = Blueprint('landing', __name__)

@landing_bp.get('/')
def landing():
    return render_template('landing.html')