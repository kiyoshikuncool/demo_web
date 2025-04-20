from flask import Blueprint, jsonify
from app.models.donation import Donation
from app.models.product import Product

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@dashboard_bp.get('/stats')
def dashboard_stats():
    total_products = Product.query.count()
    total_donations = Donation.query.count()
    return jsonify({
        'total_products': total_products,
        'total_donations': total_donations
    })
