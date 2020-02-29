from flask import Flask
from flask_dotenv import DotEnv
from flask_api import FlaskAPI

import os
from config import Config

from .extensions import db, guard, migrate

from .commands import create_users, create_database, create_breweries, create_beers, create_inventory

from .models import User, Brewery, Beer, Inventory, Order, Address

basedir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_class=Config):
    app = FlaskAPI(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)

    migrate.init_app(app,db)

    guard.init_app(app, User)

    app.cli.add_command(create_users)
    app.cli.add_command(create_database)
    app.cli.add_command(create_breweries)
    app.cli.add_command(create_beers)
    app.cli.add_command(create_inventory)
    
    from app.blueprints.api import api
    app.register_blueprint(api, url_prefix='/api')

    from flask_moment import Moment
    moment = Moment(app)
    
    with app.app_context():
        from app import models
    return app
