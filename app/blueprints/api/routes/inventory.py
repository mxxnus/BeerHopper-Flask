from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Product_Inventory, Products, Brewery

@api.route('/inventory', methods=['GET'])
def inventory():
    inven= [i.infoDict() for i in db.session.query(Product_Inventory).join(Brewery, 
    Brewery.id == Product_Inventory.brewery_id).join(Products, Products.id == Product_Inventory.product_id).all()]
    
    return jsonify(inven)

@api.route('/inventory/<int:product_id>',methods=['POST'])
def modifyInventory(product_id):
    new_id = product_id

    json_data = request.get_json()
    new_quantity = json_data['quantity']


    new_inventory = Product_Inventory.query.filter_by(product_id= new_id).first()
    new_inventory.quantity= new_quantity
    

    db.session.commit()
    return jsonify({'success' : "Inventory modified successfully"}), status.HTTP_201_CREATED



