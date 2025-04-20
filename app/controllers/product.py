from flask import Blueprint, request, jsonify
from app import db
from app.models.product import Product

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.post('/create')
def create_product():
    data = request.json
    product = Product(
        name=data['name'],
        quantity=data['quantity'],
        expiration_date=data['expiration_date'],
        location=data['location'],
        organization_id=data['organization_id']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully.'})

@product_bp.put('/<int:product_id>')
def update_product(product_id):
    data = request.json
    product = Product.query.get_or_404(product_id)
    product.name = data.get('name', product.name)
    product.quantity = data.get('quantity', product.quantity)
    product.expiration_date = data.get('expiration_date', product.expiration_date)
    product.location = data.get('location', product.location)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully.'})

@product_bp.delete('/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully.'})

@product_bp.get('/')
def list_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'quantity': p.quantity,
        'expiration_date': str(p.expiration_date),
        'location': p.location,
        'organization_id': p.organization_id
    } for p in products])

@product_bp.get('/<int:product_id>')
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'quantity': product.quantity,
        'expiration_date': str(product.expiration_date),
        'location': product.location,
        'organization_id': product.organization_id
    })