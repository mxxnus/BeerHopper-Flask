from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Beer, Inventory, Order, Address

from datetime import datetime
import random
import string

@api.route('/orders/<int:id>', methods=['GET'])
def getUserOrders(id):
    user_orders = [i.infoDict() for i in db.session.query(Order).join(Brewery, 
    Brewery.id == Order.brewery_id).join(Beer, Beer.id == Order.beer_id).join(User,
     User.id == Order.user_id).join(Address, Address.id == Order.address_id).filter_by(user_id=id).all()]
    
    return jsonify(user_orders)

@api.route('/orders', methods=['GET'])
def getOrders():
    orders = [i.infoDict() for i in db.session.query(Order).join(Brewery, 
    Brewery.id == Order.brewery_id).join(Beer, Beer.id == Order.beer_id).join(User,
     User.id == Order.user_id).join(Address, Address.id == Order.address_id).all()]
    
    return jsonify(orders)


@api.route('/orders/create', methods=['POST'])
def createOrder():
    json_data = request.get_json()

    order_number = ''.join(str(datetime.utcnow()).split())
    order_number = order_number[:10]
    order_number += randomStringDigits(6)
    
    item = json_data['item']
    quantity = json_data['quantity']
    cost = json_data['cost']
    user_id = json_data['user_id']
    beer_id = json_data['beer_id']
    brewery_id = json_data['brewery_id']
    address_id = json_data['address_id']
    
    print(order_number)

    order = Order(order_number=order_number,item=item, quantity=quantity, cost=cost, fulfilled=False,
    user_id=user_id, beer_id=beer_id, brewery_id=brewery_id, address_id=address_id)
    db.session.add(order)
    db.session.commit()

    return jsonify({'success' : "Order submitted successfully"}), status.HTTP_201_CREATED 
    

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits).upper() for i in range(stringLength))

#CREATE AN ORDER
#generate order_id timestamp + random stuff
#cost calc with order/beer_id/item/quantity * query(beer_id.cost)
#add to db
#modify inventory (same beer_id)
     