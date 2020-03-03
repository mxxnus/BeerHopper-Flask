from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(180), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    address_id = db.Column(db.Integer, nullable=False)
    address = db.relationship("Address", back_populates="user")

    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    def __repr__(self):
        return f"<User:{self.email} | {self.fname}>"

    def infoDict(self):
        data = dict(
            id=self.id,
            fname=self.fname,
            lname=self.lname,
            email=self.email,
            address=self.address.id,
            created_on=self.created_on
        )
        return data

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email.lower()).one_or_none()

   
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id



class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False)
    website = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city= db.Column(db.String(50), nullable=False)
    state= db.Column(db.String(50), nullable=False)
    zipcode= db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return f"<User:{self.email} | {self.fname}>"

    def infoDict(self):
        data = dict(
            id = self.id,
            name=self.name,
            email=self.email,
            website=self.website,
            address=self.address,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode,
            created_on=self.created_on
        )
        return data

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email.lower()).one_or_none()

   
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id


#beer = db.Table("beer",
    #db.column('brewery_id', db.Integer,db.ForeignKey('brewery.id'))
#)

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cost_sixth = db.Column(db.Float, nullable=False)
    cost_50=db.Column(db.Float, nullable=False)
    cost_half=db.Column(db.Float, nullable=False)
    cost_case=db.Column(db.Float, nullable=False)
    
    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="beer")
    
    def __repr__(self):
        return f"<User:{self.email} | {self.fname}>"

    def infoDict(self):
        
    
        data = dict(
            id = self.id,
            name=self.name,
            cost_sixth=self.cost_sixth,
            cost_50=self.cost_50,
            cost_half=self.cost_half,
            cost_case=self.cost_case,
            brewery=self.brewery.name
        )
        return data

    
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sixth = db.Column(db.Integer, nullable=False)
    L50=db.Column(db.Integer, nullable=False)
    half=db.Column(db.Integer, nullable=False)
    case=db.Column(db.Integer, nullable=False)
    
    beer_id = db.Column(db.Integer, db.ForeignKey("beer.id"))
    beer = db.relationship("Beer", back_populates="inventory")

    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="inventory")
    
    def __repr__(self):
        return f"<User:{self.id}"

    def infoDict(self):
        data = dict(
            id = self.id,
            sixth=self.sixth,
            L50=self.L50,
            half=self.half,
            case=self.case,
            brewery_id=self.brewery.id,
            brewery=self.brewery.name,
            beer_id=self.beer.id,
            beer_name=self.beer.name
        )
        return data

    
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), nullable=False)
    item = db.Column(db.String(50), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    amount=db.Column(db.Float, nullable=False)

    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow() + timedelta(days=3)) 

    status = db.Column(db.String(50), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="order")

    beer_id = db.Column(db.Integer, db.ForeignKey("beer.id"))
    beer = db.relationship("Beer", back_populates="order")

    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="order")

    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    address = db.relationship("Address", back_populates="order")
    
    def __repr__(self):
        return f"<User:{self.id}"

    def infoDict(self):
        data = dict(
            id = self.id,
            order_id=self.order_id,

            item=self.item,
            quantity=self.quantity,
            amount = self.amount,
            delivery_data=self.delivery_date,

            beer_id=self.beer.id,
            beer_name=self.beer.name,

            user_id = self.user.id,
            user_address = self.address.address,
            user_city = self.address.city,
            user_state = self.address.state,
            user_zipcode = self.address.zipcode,

            brewery_id=self.brewery.id,
            brewery=self.brewery.name,
            brewery_address= self.brewery.address,
            brewery_city= self.brewery.city,
            brewery_state= self.brewery.state,
            brewery_zipcode= self.brewery.zipcode,
            brewery_email= self.brewery.email

        )
        return data

    
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    city= db.Column(db.String(50), nullable=False)
    state= db.Column(db.String(50), nullable=False)
    zipcode= db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="address")

    def infoDict(self):
        data = dict(
            id = self.id,
            user_id=self.user.id,
            address=self.address,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode,
            created_on=self.created_on
        )
        return data

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email.lower()).one_or_none()

   
    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id


Brewery.beer = db.relationship("Beer", order_by = Beer.id, back_populates = 'brewery')
Brewery.inventory = db.relationship("Inventory", order_by = Inventory.id, back_populates = 'brewery')
Brewery.order =  db.relationship("Order", order_by = Order.id, back_populates = 'brewery')

Beer.inventory = db.relationship("Inventory", order_by = Inventory.id, back_populates = 'beer')
Beer.order = db.relationship("Order", order_by = Order.id, back_populates = 'beer')

User.order = db.relationship("Order", order_by = Order.id, back_populates = 'user')
User.address = db.relationship("Address", order_by = Address.id, back_populates = 'user')

Address.user = db.relationship("User", order_by = User.id, back_populates = 'address')
Address.order = db.relationship("Order", order_by = Order.id, back_populates = 'address')



