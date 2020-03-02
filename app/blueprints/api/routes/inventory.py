from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db
from sqlalchemy.orm.attributes import flag_modified

from app.models import User, Brewery, Beer, Inventory

@api.route('/inventory', methods=['GET'])
def inventory():
    inven= [i.infoDict() for i in db.session.query(Inventory).join(Brewery, 
    Brewery.id == Inventory.brewery_id).join(Beer, Beer.id == Inventory.beer_id).all()]
    
    return jsonify(inven)



#CHANGE BEER INVENTORY STOCK W/ POST 
@api.route('/inventory/<int:beer_id>/modify',methods=['POST'])
def modifyInventory(beer_id):
    new_id = beer_id

    json_data = request.get_json()
    new_sixth = json_data['sixth']
    new_L50 = json_data['L50']
    new_half = json_data['half']
    new_case = json_data['case']

    #newInventory = Inventory(sixth = new_sixth, L50=new_L50, half=new_half, case=new_case, beer_id=new_id,)
    inventory = Inventory.query.filter_by(beer_id = new_id).first()
    inventory.sixth = new_sixth
    inventory.L50 = new_L50
    inventory.half = new_half
    inventory.case = new_case

    db.session.commit()
    return jsonify({'success' : "success"}), status.HTTP_201_CREATED



#/inventory/<int:beer_id>/half/modify

#/inventory/<int:beer_id>/sixth/modify

#/inventory/<int:beer_id>/case/modify



