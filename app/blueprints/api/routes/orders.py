from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer, Inventory, Order, Address

@api.route('/<int:id>/orders', methods=['GET'])
def getUserOrders(id):
    inven= [i.infoDict() for i in db.session.query(Order).join(Brewery, 
    Brewery.id == Order.brewery_id).join(Beer, Beer.id == Order.beer_id).join(User,
     User.id == Order.user_id).join(Address, Address.id == Order.address_id).filter_by(user_id=id).all()]
    
    return jsonify(inven)

@api.route('/orders', methods=['GET'])
def getOrders():
    orders = [i.infoDict() for i in db.session.query(Order).join(Brewery, 
    Brewery.id == Order.brewery_id).join(Beer, Beer.id == Order.beer_id).join(User,
     User.id == Order.user_id).join(Address, Address.id == Order.address_id).all()]
    
    return jsonify(orders)

#CREATE AN ORDER
#generate order_id timestamp + random stuff
#cost calc with order/beer_id/item/quantity * query(beer_id.cost)
#add to db
#modify inventory (same beer_id)