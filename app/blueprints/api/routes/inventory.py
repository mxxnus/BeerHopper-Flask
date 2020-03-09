from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery

@api.route('/inventory', methods=['GET'])
def inventory():
    inven= [i.infoDict() for i in db.session.query(Inventory).join(Brewery, 
    Brewery.id == Inventory.brewery_id).join(Beer, Beer.id == Inventory.beer_id).all()]
    
    return jsonify(inven)

@api.route('/inventory/<int:beer_id>/modify',methods=['POST'])
def modifyInventory(beer_id):
    new_id = beer_id

    json_data = request.get_json()
    new_sixth = json_data['sixth']
    new_L50 = json_data['L50']
    new_half = json_data['half']
    new_case = json_data['case']

    new_inventory = Inventory.query.filter_by(beer_id = new_id).first()
    new_inventory.sixth = new_sixth
    new_inventory.L50 = new_L50
    new_inventory.half = new_half
    new_inventory.case = new_case

    db.session.commit()
    return jsonify({'success' : "Inventory modified successfully"}), status.HTTP_201_CREATED



