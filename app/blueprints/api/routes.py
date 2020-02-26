from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User


@api.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    if email == "":
        return jsonify({'email' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST
    elif password == "":
        return jsonify({'password' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST
    user = guard.authenticate(email, password)
    token = guard.encode_jwt_token(user)
    return jsonify({'access_token' : token})

@api.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    
    email = json_data['email']
    if email == "":
        return jsonify({'email' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    password = json_data['password']
    if password == "":
        return jsonify({'password' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    confirmPassword = json_data['confirmPassword']
    if confirmPassword == "":
        return jsonify({'confirmPassword' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    fname = json_data['fname']
    if fname == "":
        return jsonify({'fname' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    lname = json_data['lname']
    if lname == "":
        return jsonify({'lname' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    organization_id = json_data['organization_id']
    if organization_id == "":
        return jsonify({'organization_id' : "Must not be empty", 'status_code':400}), status.HTTP_400_BAD_REQUEST

    user = User(email=email.lower() , fname=fname, lname=lname,
    organization_id=organization_id, password=guard.hash_password(password))

    #print(type(user.identify))
    if password != confirmPassword:
        return jsonify({'error' : "AuthenticationError", "message":"Passwords must match",'status_code':400}), status.HTTP_400_BAD_REQUEST

    elif user.lookup(user.email) != None:
        return jsonify({'error' : "AuthenticationError", "message":"Email is already is use",'status_code':400}), status.HTTP_400_BAD_REQUEST

    
    elif password == confirmPassword and user.lookup(user.email) == None:
        db.session.add(user)
        db.session.commit()
        user = guard.authenticate(email, password)
        token = guard.encode_jwt_token(user)

        return jsonify({'access_token' : token}), status.HTTP_201_CREATED



@api.route('/protected')
@auth_required
def protected():
    return jsonify({'result' : 'You are in a special area!'}) 


@api.route('/open')
def open():
    return jsonify({'result' : 'Hello'})