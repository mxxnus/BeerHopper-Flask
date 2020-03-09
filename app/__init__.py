from flask import Flask
from flask_dotenv import DotEnv
from flask_api import FlaskAPI

import os
from config import Config

from .extensions import db, guard, migrate

from .commands import create_users, create_database, create_breweries, create_products, create_inventory, create_addresses, create_orders

from .models import User

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
    app.cli.add_command(create_products)
    app.cli.add_command(create_inventory)
    app.cli.add_command(create_addresses)
    app.cli.add_command(create_orders)


    from app.blueprints.api import api
    app.register_blueprint(api, url_prefix='/api')

    from flask_moment import Moment
    moment = Moment(app)
    
    with app.app_context():
        from app import models
    return app
