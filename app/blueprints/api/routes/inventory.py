from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer, Inventory

@api.route('/inventory', methods=['GET'])
def inventory():
    inven= [i.infoDict() for i in db.session.query(Inventory).join(Brewery, 
    Brewery.id == Inventory.brewery_id).join(Beer, Beer.id == Inventory.beer_id).all()]
    
    return jsonify(inven)



#CHANGE BEER INVENTORY STOCK W/ POST 

#/inventory/<int:beer_id>/L50/modify

#/inventory/<int:beer_id>/half/modify

#/inventory/<int:beer_id>/sixth/modify

#/inventory/<int:beer_id>/case/modify



