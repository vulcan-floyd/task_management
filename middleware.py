import jwt
from flask import request, jsonify, current_app, g
from  werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models.model import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
            g.user_id = current_user.id
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  f(*args, **kwargs)
  
    return decorated