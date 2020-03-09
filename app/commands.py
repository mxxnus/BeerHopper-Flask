import click 
from flask.cli import with_appcontext 

from .extensions import guard, db
from .models import User, Brewery, Products, Product_Inventory, Address, Customer_Orders, Customer_Order_Products, Product_Prices

@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
    one = User(email="user1@email.com" , fname="Derek", lname="Moon", address_id=1, password=guard.hash_password('one'))
    two = User(email="user2@email.com" , fname="Chad", lname="Coomes", address_id=2, password=guard.hash_password('two'))
    three = User(email="user3@email.com" , fname="George", lname="Troutman", address_id=3, password=guard.hash_password('three'))

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_breweries')
@with_appcontext
def create_breweries():
    one = Brewery(email="madmoon@email.com" ,address="2138 Britains Lane", city="Columbus", state="Ohio", zipcode="43031", name="MadMoon",website="https://madmooncider.com/",  password=guard.hash_password('one'))
    two = Brewery(email="lineage@email.com" , address="2971 N High St", city="Columbus", state="Ohio", zipcode="43202",name="Lineage", website="https://www.lineagebrew.com/", password=guard.hash_password('two'))
    three = Brewery(email="brewdogs@email.com", address="96 Gender Rd", city="Canal Winchester", state="Ohio", zipcode="43110",  name="Brew Dogs", website="https://www.brewdog.com/uk/",password=guard.hash_password('three'))

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_products')
@with_appcontext
def create_products():
    one = Products(name="HopWired",brewery_id=1, product_type=1)
    two = Products(name="HopWired",brewery_id=1, product_type=2)
    three = Products(name="HopWired",brewery_id=1, product_type=3)


    #five = Products(name="Pale Ale",brewery_id=2, product_type=1)
    #six = Products(name="Pale Ale",brewery_id=2, product_type=2 )
    #seven = Products(name="Pale Ale", brewery_id=2, product_type=3)

    five = Products(name="Indian Pale Ale",brewery_id=3, product_type=1)
    six = Products(name="Indian Pale Ale",brewery_id=3, product_type=2 )
    seven = Products(name="Indian Pale Ale", brewery_id=3, product_type=3)

    db.session.add_all([ one, two, three, five, six, seven])
    db.session.commit()

@click.command(name='create_inventory')
@with_appcontext
def create_inventory():
    one = Product_Inventory(brewery_id=1, quantity=30 ,product_id=5,)
    two= Product_Inventory(brewery_id=1, quantity=30 ,product_id=6,)
    three = Product_Inventory(brewery_id=1, quantity=30 ,product_id=7,)

    four = Product_Inventory(brewery_id=2, quantity=100 ,product_id=8)
    five = Product_Inventory(brewery_id=2, quantity=100 ,product_id=9)
    six = Product_Inventory(brewery_id=2, quantity=100 ,product_id=10)

    seven = Product_Inventory(brewery_id=3, quantity=300 ,product_id=11)
    eight = Product_Inventory(brewery_id=3, quantity=300 ,product_id=12)
    nine = Product_Inventory(brewery_id=3, quantity=300 ,product_id=13)

    db.session.add_all([four,five,six,seven,eight,nine])
    db.session.commit()

@click.command(name='create_addresses')
@with_appcontext
def create_addresses():
    one = Address(user_id=1,address="4205 Weaverton Lane",city="Columbus",state="Ohio", zipcode="43219")
    two = Address(user_id=2,address="743 Parsons Ave",city="Columbus",state="Ohio", zipcode="43206")
    three = Address(user_id=3,address="5511 New Albany Rd",city="New Albany",state="Ohio", zipcode="43054")

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_orders')
@with_appcontext
def create_orders():
    one = Customer_Orders(order_number="1", cost=100 , status="Unfulfilled", user_id=1, 
     brewery_id=1, address_id=1)
   

    two = Customer_Orders(order_number="2", cost=500 , status="Unfulfilled", user_id=2, 
     brewery_id=2, address_id=2)

    three = Customer_Orders(order_number="3", cost=750 , status="Unfulfilled", user_id=3, 
     brewery_id=3, address_id=3)

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_orders_products')
@with_appcontext
def create_orders_products():
    one = Customer_Order_Products(order_id="1", product_id = 5, quantity=1)
    two = Customer_Order_Products(order_id="2", product_id = 10, quantity=3)
    three = Customer_Order_Products(order_id="3", product_id = 13, quantity=3)
    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_product_prices')
@with_appcontext
def create_product_prices():
    product_prices = []
    one = product_prices.append(Product_Prices( product_id = 5, price =35.00 ))
    two = product_prices.append(Product_Prices( product_id = 6 , price =95.00 ))
    three = product_prices.append(Product_Prices( product_id = 7, price =120.00 ))
    four = product_prices.append(Product_Prices( product_id = 8, price =30.00 ))
    five = product_prices.append(Product_Prices( product_id = 9, price = 85.00))
    six = product_prices.append(Product_Prices( product_id = 10, price = 95.00))
    seven = product_prices.append(Product_Prices( product_id = 11, price = 28.00))
    eight = product_prices.append(Product_Prices( product_id = 12, price = 75.00))
    nine = product_prices.append(Product_Prices( product_id = 13, price = 90.00))

    
    db.session.add_all(product_prices)
    db.session.commit()