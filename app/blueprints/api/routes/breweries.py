from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer, Inventory

@api.route('/breweries', methods=['GET'])
def breweries():
    breweries= [i.infoDict() for i in Brewery.query.all()]
    
    return jsonify(breweries)

