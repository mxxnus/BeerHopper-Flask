from flask import jsonify, request

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard



@api.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']
    user = guard.authenticate(username, password)
    token = guard.encode_jwt_token(user)
    
    print(token)
    return jsonify({'access_token' : token})


@api.route('/protected')
@auth_required
def protected():
    return jsonify({'result' : 'You are in a special area!'}) 


@api.route('/open')
def open():
    return jsonify({'result' : 'Hello'})