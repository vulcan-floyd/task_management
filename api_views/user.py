from flask import Flask, request, jsonify, make_response, Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from extensions import db
from models.model import User
from flasgger.utils import swag_from

api_user_blueprint = Blueprint('api_user_blueprint', __name__)


@swag_from("api_docs/user/home.yml")
@api_user_blueprint.route('/', methods =['GET'])
def home():
   return jsonify({"data": "HomePage"})

@swag_from("api_docs/user/login.yml")
@api_user_blueprint.route('/login', methods =['POST'])
def login_user():
    
    content = request.get_json()
    username = content['name']
    password = content['password']
 
    user = User.query.filter_by(name=username).first()
    print(user)
    if check_password_hash(user.password, password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.utcnow() + timedelta(minutes=45)}, current_app.config['SECRET_KEY'], "HS256")
 
        return jsonify({'token' : token})
 
    return make_response('could not verify',  401, {'Authentication': '"login required"'})


@swag_from("api_docs/user/signup.yml")
@api_user_blueprint.route('/signup', methods =['POST'])
def signup_user(): 
    data = request.get_json() 
    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user) 
    db.session.commit()
    return jsonify({'message': 'registered successfully'})
    
    

@swag_from("api_docs/user/users.yml")
@api_user_blueprint.route('/users', methods =['GET'])
def get_all_users(): 
   users = User.query.all()
   result = []  
   for user in users:  
       user_data = {}  
       user_data['public_id'] = user.public_id 
       user_data['name'] = user.name
       user_data['password'] = user.password
       user_data['admin'] = user.admin
     
       result.append(user_data)  
   return jsonify({'users': result})


@swag_from("api_docs/user/users-promote.yml")
@api_user_blueprint.route('/users/<public_id>', methods =['PUT'])
def promote_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
   
    if not user:
        return jsonify({'message': 'No user Found'})
    
    user.admin = 1
    db.session.commit()
    
    return jsonify({'message': 'User has been promoted'})
