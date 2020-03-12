from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Address, Brewery, Products, Product_Inventory, Product_Prices, Customer_Order_Products, Customer_Orders

from datetime import datetime
import random
import string



@api.route('/orders', methods=['GET'])
def getUserOrders():
    header = request.headers['Authorization']
    auth_token = header.split()[1]
    jwt_data = guard.extract_jwt_token(auth_token)
    id = jwt_data['id']

    user_orders = [i.infoDict() for i in db.session.query(Customer_Orders).join(Brewery, 
    Brewery.id == Customer_Orders.brewery_id).join(User,User.id == Customer_Orders.user_id)
    .join(Address, Address.id == Customer_Orders.address_id).filter_by(user_id=id).all()]

    return jsonify(user_orders)

'''

#includes products by calling a Customer_Order_Products method in the Customer_Orders class
@api.route('/orders', methods=['GET'])
def getOrders():
    
    orders = [i.infoDict() for i in db.session.query(Customer_Orders).join(Brewery, 
    Brewery.id == Customer_Orders.brewery_id).join(User,
    User.id == Customer_Orders.user_id).join(Address, Address.id == Customer_Orders.address_id)
    .all()]

    return jsonify(orders)
'''



@api.route('/orders/create', methods=['POST'])
def createOrder():
    #Destructure req header
    header = request.headers['Authorization']
    auth_token = header.split()[1]
    jwt_data = guard.extract_jwt_token(auth_token)
    user_id = jwt_data['id']

    #generate order number
    order_number = ''.join(str(datetime.utcnow()).split())
    order_number = order_number[:10]
    order_number += randomStringDigits(6)

    #generate order id 
    order_id = randomDigits(8)

    #Get rest of order details from req json
    json_data = request.get_json()
    cost = json_data['cost']
    brewery_id = json_data['brewery_id']
    address_id = json_data['address_id']

    order = Customer_Orders(id = order_id, order_number=order_number,
    cost=cost, status="Unfulfilled",user_id=user_id,brewery_id=brewery_id, 
    address_id=address_id)

    db.session.add(order)


    #Gets products from req json to add to Customer_Order_Products table
    products = json_data['products']
    products_list = []

    for i in products:
        product_id = i['product_id']
        quantity = i['quantity']
        customer_order_products = Customer_Order_Products(order_id = order_id, product_id=product_id, quantity=quantity, order_number = order_number)
        products_list.append(customer_order_products)

        #Subtracts quantities from products_inventory table
        old_product_inventory = Product_Inventory.query.filter_by(product_id = product_id).first()
        old_product_inventory.quantity -= quantity

    db.session.add_all(products_list)

    db.session.commit()


    return jsonify({'success' : "Order submitted successfully"}), status.HTTP_201_CREATED 


def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits).upper() for i in range(stringLength))

def randomDigits(stringLength=8):
    """Generate a random string of letters and digits """
    onlyDigits =  string.digits
    return ''.join(random.choice(onlyDigits) for i in range(stringLength))

    '''
    sixth_quantity = int(json_data['sixth_quantity'])
    L50_quantity = int(json_data['L50_quantity'])
    half_quantity = int(json_data['half_quantity'])
    case_quantity = int(json_data['case_quantity'])

    if sixth_quantity == 0 and L50_quantity == 0 and half_quantity == 0 and case_quantity == 0:
        return jsonify({ 'error' : "FormError", "message":"Please add items to your order",'status_code':400}), status.HTTP_400_BAD_REQUEST
    
    elif sixth_quantity == "" or L50_quantity == "" or half_quantity == "" or case_quantity == "":
        return jsonify({ 'error' : "FormError", "message":"Please add items to your order",'status_code':400}), status.HTTP_400_BAD_REQUEST


    cost = json_data['cost']
    beer_id = json_data['beer_id']
    print(beer_id)

    #from beer id will be able to get these
    brewery_id = json_data['brewery_id']
    address_id = json_data['address_id']
    
    print(order_number)

    order = Order(order_number=order_number, sixth_quantity=sixth_quantity, 
    L50_quantity=L50_quantity, half_quantity=half_quantity,case_quantity=case_quantity,
    cost=cost, fulfilled=False,user_id=user_id, beer_id=beer_id, brewery_id=brewery_id, 
    address_id=address_id)

    old_inventory = Inventory.query.filter_by(beer_id = beer_id).first()

    old_inventory.sixth -=  sixth_quantity
    old_inventory.L50 -=  L50_quantity
    old_inventory.half -=  half_quantity
    old_inventory.case -=  case_quantity

    db.session.commit()
    return jsonify({'success' : "Order submitted successfully"}), status.HTTP_201_CREATED 
    
'''