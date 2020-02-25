from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian 
from flask_migrate import Migrate

db = SQLAlchemy()
guard = Praetorian()
migrate = Migrate()
