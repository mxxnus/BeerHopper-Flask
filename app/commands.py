import click 
from flask.cli import with_appcontext 

from .extensions import guard, db
from .models import User, Brewery

@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
    one = User(email="user1@email.com" , fname="Derek", lname="Moon", organization_id=1, password=guard.hash_password('one'))
    two = User(email="user2@email.com" , fname="Chad", lname="Coomes", organization_id=1, password=guard.hash_password('two'))
    three = User(email="user3@email.com" , fname="George", lname="Troutman", organization_id=1, password=guard.hash_password('three'))

    db.session.add_all([one, two, three])
    db.session.commit()

@click.command(name='create_breweries')
@with_appcontext
def create_breweries():
    one = Brewery(email="madmoon@email.com" ,address="2138 Britains Lane", city="Columbus", state="Ohio", zipcode="43031", name="MadMoon",website="https://madmooncider.com/", organization_id=1, password=guard.hash_password('one'))
    two = Brewery(email="lineage@email.com" , address="2971 N High St", city="Columbus", state="Ohio", zipcode="43202",name="Lineage", website="https://www.lineagebrew.com/", organization_id=2,password=guard.hash_password('two'))
    three = Brewery(email="brewdogs@email.com", address="96 Gender Rd", city="Canal Winchester", state="Ohio", zipcode="43110",  name="Brew Dogs", website="https://www.brewdog.com/uk/",organization_id=3,password=guard.hash_password('three'))

    db.session.add_all([one, two, three])
    db.session.commit()
    