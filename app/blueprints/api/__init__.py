from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates/api', static_folder='static')

from app.blueprints.api import routes