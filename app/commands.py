import click 
from flask.cli import with_appcontext 

from .extensions import guard, db
from .models import User, Brewery, Beer, Inventory, Address, Order

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

@click.command(name='create_beers')
@with_appcontext
def create_beers():
    one = Beer(name="HopWired",brewery_id=8, cost_sixth= 45, cost_50=120, cost_half=150, cost_case=44.99)
    two = Beer(name="Lineage Pale Ale",brewery_id=9, cost_sixth=40 , cost_50=100, cost_half=140, cost_case=34.99)
    three = Beer(name="Brew Dogs Indian Pale Ale", brewery_id=10, cost_sixth=35, cost_50=96, cost_half=135, cost_case=32.99)

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_inventory')
@with_appcontext
def create_inventory():
    one = Inventory(brewery_id=8, sixth= 5, L50=10, half=0, case=45, beer_id=3,)
    two = Inventory(brewery_id=9, sixth=34 , L50=43, half=3, case=255, beer_id=4)
    three = Inventory(brewery_id=10, sixth=199, L50=323, half=23, case=899, beer_id=5)

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_addresses')
@with_appcontext
def create_addresses():
    one = Address(user_id=18,address="4205 Weaverton Lane",city="Columbus",state="Ohio", zipcode="43219")
    two = Address(user_id=19,address="743 Parsons Ave",city="Columbus",state="Ohio", zipcode="43206")
    three = Address(user_id=20,address="5511 New Albany Rd",city="New Albany",state="Ohio", zipcode="43054")

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_orders')
@with_appcontext
def create_orders():
    one = Order(order_id="1",item="L50", quantity=3, amount=129.99, status="Unfullfilled",user_id=18, beer_id=3, brewery_id=8, address_id=1)
    two = Order(order_id="1",item="case", quantity=5, amount=250.00, status="Unfullfilled",user_id=18, beer_id=3, brewery_id=8, address_id=1)
    three = Order(order_id="1",item="case", quantity=10, amount=100, status="Unfullfilled",user_id=19, beer_id=5, brewery_id=10, address_id=2)

    db.session.add_all([one, two, three])
    db.session.commit()