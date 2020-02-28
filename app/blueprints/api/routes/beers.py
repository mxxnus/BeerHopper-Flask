from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer

@api.route('/beers', methods=['GET'])
def beers():

    beers= [i.infoDict() for i in Beer.query.all()]
    
    return jsonify(beers)
    

