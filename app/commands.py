import click 
from flask.cli import with_appcontext 

from .extensions import guard, db
from .models import User

@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
    one = User(username='One',     email="user1@email.com" , fname="Derek", lname="Moon", organization_id=1, password=guard.hash_password('one'))
    two = User(username='Two',     email="user2@email.com" , fname="Chad", lname="Coomes", organization_id=1, password=guard.hash_password('two'))
    three = User(username='Three', email="user3@email.com" , fname="George", lname="Troutman", organization_id=1, password=guard.hash_password('three'))

    db.session.add_all([one, two, three])
    db.session.commit()