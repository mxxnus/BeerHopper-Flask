from app import create_app, db
from app.models import User, Brewery, Products, Product_Inventory, Address, Customer_Orders, Customer_Order_Products

app = create_app()

@app.shell_context_processor
def get_context():
    return dict(User = User, Brewery=Brewery, Products=Products, Customer_Order_Products=Customer_Order_Products, Product_Inventory=Product_Inventory, Address=Address, app=app, db=db)