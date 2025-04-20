from flask import Blueprint, request, jsonify
from app import db
from app.models.donation import Donation

donation_bp = Blueprint('donation', __name__, url_prefix='/api/donations')

@donation_bp.post('/')
def create_donation():
    data = request.json
    donation = Donation(
        product_id=data['product_id'],
        donor_id=data['donor_id'],
        recipient_id=data['recipient_id'],
        quantity=data['quantity']
    )
    db.session.add(donation)
    db.session.commit()
    return jsonify({'message': 'Donation recorded successfully.'})

@donation_bp.put('/<int:donation_id>')
def update_donation(donation_id):
    data = request.json
    donation = Donation.query.get_or_404(donation_id)
    donation.product_id = data.get('product_id', donation.product_id)
    donation.donor_id = data.get('donor_id', donation.donor_id)
    donation.recipient_id = data.get('recipient_id', donation.recipient_id)
    donation.quantity = data.get('quantity', donation.quantity)
    db.session.commit()
    return jsonify({'message': 'Donation updated successfully.'})

@donation_bp.delete('/<int:donation_id>')
def delete_donation(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    db.session.delete(donation)
    db.session.commit()
    return jsonify({'message': 'Donation deleted successfully.'})

@donation_bp.get('/')
def list_donations():
    donations = Donation.query.all()
    return jsonify([{
        'id': d.id,
        'product_id': d.product_id,
        'donor_id': d.donor_id,
        'recipient_id': d.recipient_id,
        'quantity': d.quantity,
        'donated_at': d.donated_at.isoformat()
    } for d in donations])

@donation_bp.get('/<int:donation_id>')
def get_donation(donation_id):
    donation = Donation.query.get_or_404(donation_id)
    return jsonify({
        'id': donation.id,
        'product_id': donation.product_id,
        'donor_id': donation.donor_id,
        'recipient_id': donation.recipient_id,
        'quantity': donation.quantity,
        'donated_at': donation.donated_at.isoformat()
    })