from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer

@api.route('/beers', methods=['GET'])
def beers():
    #[i.infoDict() for i in Beer.query.all()]
    beers= [i.infoDict() for i in db.session.query(Beer).join(Brewery, 
    Brewery.id == Beer.brewery_id).all()]
    
    return jsonify(beers)
    

