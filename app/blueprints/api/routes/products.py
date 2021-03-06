from flask import jsonify, request
from flask_api import status

from app.blueprints.api import api

from flask_praetorian import auth_required
from app.extensions import guard, db

from app.models import User, Brewery, Products, Product_Prices

@api.route('/products', methods=['GET'])
def products():
    #[i.infoDict() for i in Beer.query.all()]
    
    products= [i.infoDict() for i in db.session.query(Products).join(Brewery, 
    Brewery.id == Products.brewery_id).join(Product_Prices, Product_Prices.id == Products.price_id).all()]

    return jsonify(products)
    
    
    
    
@api.route('/unique_products', methods=['GET'])
def unique_products():
    
    products= [i.infoDict() for i in db.session.query(Products).distinct(Products.name).join(Brewery, 
    Brewery.id == Products.brewery_id).join(Product_Prices, Product_Prices.id == Products.price_id).all()]

    return jsonify(products)    
    

#case sensitive
@api.route('/products/<product_name>', methods=['GET'])
def one_product(product_name):
    
    products= [i.infoDict() for i in db.session.query(Products).filter_by(name=product_name).join(Brewery, 
    Brewery.id == Products.brewery_id).join(Product_Prices, Product_Prices.id == Products.price_id).all()]

    return jsonify(products)    
    '''
    




#change the price    
#/beer/beer_id/
'''
