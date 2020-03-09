from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Products

@api.route('/products', methods=['GET'])
def products():
    #[i.infoDict() for i in Beer.query.all()]
    products= [i.infoDict() for i in db.session.query(Products).join(Brewery, 
    Brewery.id == Products.brewery_id).all()]
    
    return jsonify(products)

#change the price    
#/beer/beer_id/

