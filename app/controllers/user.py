from flask import Blueprint, request, jsonify
from app import app, db
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)  # Blueprint for modularity

# @user_bp.route('/register', methods=['POST']) # Cơ bản
@user_bp.post('/register') # Đã quen
def register():
    data = request.get_json()
    
    # Validate email format
    if '@' not in data['email']:
        return jsonify(message="Invalid email format"), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify(message="Email already exists"), 400

    hashed_pw = User.hash_password(data['password'])
    new_user = User(email=data['email'], name=data['name'], password=hashed_pw, role=data['role'])
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

# @user_bp.route('/login', methods=['POST']) # Cơ bản
@user_bp.post('/login') # Đã quen
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and User.verify_password(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, email=user.email, name=user.name), 200

    return jsonify(message="Invalid credentials"), 401

# @user_bp.route('/profile', methods=['GET'])  # Cơ bản
@user_bp.get('/profile') # Đã quen
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify(message="User not found"), 404

    return jsonify(email=user.email, name=user.name, role=user.role), 200