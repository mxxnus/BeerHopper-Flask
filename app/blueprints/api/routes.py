from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard

from app.models import User


@api.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    user = guard.authenticate(email, password)
    token = guard.encode_jwt_token(user)
    
    print(token)
    return jsonify({'access_token' : token})

@api.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    email = json_data['email']
    username = json_data['username']
    password = json_data['password']
    confirmPassword = json_data['confirmPassword']
    fname = json_data['fname']
    lname = json_data['lname']
    organization_id = json_data['organization_id']
    user = User(username=username, email=email , fname=fname, lname=lname,
    organization_id=organization_id, password=guard.hash_password(password))

    #print(type(user.identify))
    if password != confirmPassword:
        return jsonify({'error' : 'Passwords must match'}), status.HTTP_400_BAD_REQUEST

    elif user.lookup(user.email) != None:
        return jsonify({'error' : 'Email already is use'}), status.HTTP_400_BAD_REQUEST

    elif user.username_lookup(user.username) != None:
        return jsonify({'error' : 'Username already is use'}), status.HTTP_400_BAD_REQUEST

    elif password == confirmPassword and user.lookup(user.email) == None:
        return jsonify({'result' : 'Hello'}), status.HTTP_201_CREATED


@api.route('/protected')
@auth_required
def protected():
    return jsonify({'result' : 'You are in a special area!'}) 


@api.route('/open')
def open():
    return jsonify({'result' : 'Hello'})