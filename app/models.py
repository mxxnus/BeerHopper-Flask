from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

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
            address=self.address_id,
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

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)

    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="products")
    
    def __repr__(self):
        return f"<User:{self.email} | {self.fname}>"

    def infoDict(self):
        data = dict(
            id = self.id,
            name=self.name,
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


class Product_Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer,nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    products = db.relationship("Products", back_populates="product_inventory")

    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="product_inventory")
    
    def __repr__(self):
        return f"<User:{self.id}"

    def infoDict(self):
        data = dict(
            id = self.id,
            brewery_id=self.brewery.id,
            brewery=self.brewery.name,
            product_id=self.products.id,
            product_name=self.products.name,
            product_type=self.products.product_type,
            quantity=self.quantity
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
    

class Customer_Orders(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True,)
    order_number = db.Column(db.String(50), nullable=False,   unique=True)
    
    
    cost=db.Column(db.Float, nullable=False)

    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow() + timedelta(days=3)) 

    status = db.Column(db.String(50), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="customer_orders")

    brewery_id = db.Column(db.Integer, db.ForeignKey("brewery.id"))
    brewery = db.relationship("Brewery", back_populates="customer_orders")

    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    address = db.relationship("Address", back_populates="customer_orders")

    #products_list = db.relationship('Customer_Order_Products', backref="customer_orders",
    #cascade="all, delete-orphan" , lazy='dynamic')
    
    def __repr__(self):
        return f"<User:{self.id}"

    def infoDict(self):
        order_id=self.id

        products_data = [i.productDict() for i in db.session.query(Customer_Order_Products).filter_by(order_id=order_id).all()]
        

        brewery_data = dict(
            brewery_id=self.brewery.id,
            brewery=self.brewery.name,
            brewery_address= self.brewery.address,
            brewery_city= self.brewery.city,
            brewery_state= self.brewery.state,
            brewery_zipcode= self.brewery.zipcode,
            brewery_email= self.brewery.email
        )
        user_data = dict(
            user_id = self.user.id,
            user_address = self.address.address,
            user_city = self.address.city,
            user_state = self.address.state,
            user_zipcode = self.address.zipcode
        )

        data = dict(
            id = self.id,
            order_number=self.order_number,

            products = products_data,

            cost = self.cost,
            delivery_date=self.delivery_date,
            created_on = self.created_on,
            status = self.status,

            brewery_data = brewery_data,
            user_data =  user_data
        
        )
        return data



class Customer_Order_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_number = db.Column(db.String(50),nullable=False )

    #note the double underscore below.. maybe should bring in table names as var
    order_id = db.Column(db.String(50), db.ForeignKey("customer__orders.id"))
    customer_orders = db.relationship("Customer_Orders", back_populates="customer_order_products")

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    products = db.relationship("Products", back_populates="customer_order_products")

    def productDict(self):
        product_Data = dict(
            product_id = self.product_id,
            quantity = self.quantity
        )
        return product_Data
        

class Product_Prices(db.Model):
    date_from = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    price = db.Column(db.Float, nullable=False)

    product_id = db.Column(db.Integer,  db.ForeignKey("products.id"), primary_key=True)
    products = db.relationship("Products", back_populates="product_prices")





Brewery.products = db.relationship("Products", order_by = Products.id, back_populates = 'brewery')
Brewery.product_inventory = db.relationship("Product_Inventory", order_by = Product_Inventory.id, back_populates = 'brewery')
Brewery.customer_orders =  db.relationship("Customer_Orders", order_by = Customer_Orders.id, back_populates = 'brewery')

Products.product_inventory = db.relationship("Product_Inventory", order_by = Product_Inventory.id, back_populates = 'products')
Products.customer_order_products = db.relationship("Customer_Order_Products", order_by = Customer_Order_Products.id, back_populates = 'products' )
Products.product_prices = db.relationship("Product_Prices",  order_by = Product_Prices.product_id, back_populates = 'products' )

User.customer_orders = db.relationship("Customer_Orders", order_by = Customer_Orders.id, back_populates = 'user')
User.address = db.relationship("Address", order_by = Address.id, back_populates = 'user')

Address.user = db.relationship("User", order_by = User.id, back_populates = 'address')
Address.customer_orders = db.relationship("Customer_Orders", order_by = Customer_Orders.id, back_populates = 'address')

Customer_Orders.customer_order_products = db.relationship("Customer_Order_Products", order_by = Customer_Order_Products.order_id, back_populates = 'customer_orders' )



