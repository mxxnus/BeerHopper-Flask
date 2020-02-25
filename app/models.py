from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#fname = db.Column(db.String(50), nullable=False)
#lname = db.Column(db.String(50), nullable=False)
#email = db.Column(db.String(50), nullable=False, unique=True)
# organization_id = db.Column(db.Integer, nullable=False)
#created_on = db.Column(db.DateTime, nullable=False,
                           #default=datetime.utcnow)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(180), nullable=False)
   
    #def __repr__(self):
        #return f"<User:{self.name} | {self.email}>"

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id