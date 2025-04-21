from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('user', __name__, url_prefix='/api/auth')  # Blueprint for modularity

# @auth_bp.route('/register', methods=['POST']) # Cơ bản
@auth_bp.post('/register') # Đã quen
def register():
    data = request.get_json()
    
    # Validate email format
    if '@' not in data['email']:
        return jsonify(message="Invalid email format"), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify(message="Email already exists"), 400

    hashed_pw = User.hash_password(data['password'])
    new_user = User(
        email=data['email'],
        phoneNumber=data['phoneNumber'],
        address=data['address'],
        type=data['type'],
        name=data['name'],
        password=hashed_pw,
        role=data['role']
    )
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

# @auth_bp.route('/login', methods=['POST']) # Cơ bản
@auth_bp.post('/login') # Đã quen
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and User.verify_password(user.password, data['password']):
        access_token = create_access_token(identity=str(user.id)) # Vì id đang là số, đầu vô token là string (chuỗi)
        return jsonify(access_token=access_token, email=user.email, name=user.name), 200

    return jsonify(message="Invalid credentials"), 401

# @auth_bp.route('/profile', methods=['GET'])  # Cơ bản
@auth_bp.get('/profile') # Đã quen
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify(message="User not found"), 404

    return jsonify(email=user.email, name=user.name, role=user.role), 200