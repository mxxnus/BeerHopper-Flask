from app import create_app, db
from app.models import User, Brewery, Product_Inventory, Products

app = create_app()

@app.shell_context_processor
def get_context():
    return dict(User = User, Brewery=Brewery, Products=Products, Product_Inventory=Product_Inventory,app=app, db=db)