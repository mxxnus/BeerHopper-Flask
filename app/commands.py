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
    one = Products(name="HopWired",brewery_id=1, product_type=1, price_id=20)
    two = Products(name="HopWired",brewery_id=1, product_type=2, price_id=21)
    three = Products(name="HopWired",brewery_id=1, product_type=3, price_id=22)


    five = Products(name="Pale Ale",brewery_id=2, product_type=1, price_id=23)
    six = Products(name="Pale Ale",brewery_id=2, product_type=2 , price_id=24)
    seven = Products(name="Pale Ale", brewery_id=2, product_type=3, price_id=25)

    eight = Products(name="Indian Pale Ale",brewery_id=3, product_type=1, price_id=26)
    nine = Products(name="Indian Pale Ale",brewery_id=3, product_type=2 , price_id=27)
    ten = Products(name="Indian Pale Ale", brewery_id=3, product_type=3, price_id=28)

    db.session.add_all([ one, two, three, five, six, seven, eight, nine, ten])
    db.session.commit()

@click.command(name='create_inventory')
@with_appcontext
def create_inventory():
    one = Product_Inventory(brewery_id=1, quantity=30 ,product_id=15,)
    two= Product_Inventory(brewery_id=1, quantity=30 ,product_id=16,)
    three = Product_Inventory(brewery_id=1, quantity=30 ,product_id=17,)

    four = Product_Inventory(brewery_id=2, quantity=100 ,product_id=18)
    five = Product_Inventory(brewery_id=2, quantity=100 ,product_id=19)
    six = Product_Inventory(brewery_id=2, quantity=100 ,product_id=20)

    seven = Product_Inventory(brewery_id=3, quantity=300 ,product_id=21)
    eight = Product_Inventory(brewery_id=3, quantity=300 ,product_id=22)
    nine = Product_Inventory(brewery_id=3, quantity=300 ,product_id=23)

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
    four = Customer_Order_Products(order_id="3", product_id = 12, quantity=2)

    db.session.add_all([one, two, three, four])
    db.session.commit()

@click.command(name='create_product_prices')
@with_appcontext
def create_product_prices():
    product_prices = []
    one = product_prices.append(Product_Prices( id =20 , price =35.00 ))
    two = product_prices.append(Product_Prices( id =21 , price =95.00 ))
    three = product_prices.append(Product_Prices( id =22 ,price =120.00 ))
    four = product_prices.append(Product_Prices(id =23 , price =30.00 ))
    five = product_prices.append(Product_Prices( id =24 ,price = 85.00))
    six = product_prices.append(Product_Prices( id =25 ,price = 95.00))
    seven = product_prices.append(Product_Prices( id =26 ,price = 28.00))
    eight = product_prices.append(Product_Prices( id =27 ,price = 75.00))
    nine = product_prices.append(Product_Prices(id =28 , price = 90.00))

    
    db.session.add_all(product_prices)
    db.session.commit()