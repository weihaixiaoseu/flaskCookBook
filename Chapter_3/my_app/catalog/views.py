from decimal import Decimal
from flask import request, Blueprint, jsonify
# from my_app.catalog.models import Product
from my_app.catalog.models import Product, Category
from my_app import db
from my_app import redis

catalog = Blueprint('catalog', __name__)

 
@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."

# get_or_404(PK)
@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    product_key = 'product-%s' % product.id
    # product_key = 'testkey'
    redis.set(product_key, product.name)
    redis.expire(product_key, 600)
    return 'Product - %s, $%s' % (product.name, product.price)

@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category.name
        }
    return jsonify(res)

@catalog.route('/product-create', methods=['POST',])
def create_product():  
    name = request.form.get('name')
    price = request.form.get('price')
    categ_name = request.form.get('category')
    category = Category.query.filter_by(name=categ_name).first()
    if not category:
        category = Category(categ_name)
    product = Product(name, price, category)
    db.session.add(product)
    # db.session.commit()
    return 'Product created.' 

@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    # db.session.commit()
    return 'Category created.'

@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
        res[category.id] = {'name': category.name }
        res[category.id]['products'] = []
        for product in category.products:
            res[category.id]['products'].extend([{
            'id': product.id,
            'name': product.name,
            'price': product.price
            }])
    return jsonify(res)

@catalog.route('/recent-products')
def recent_products():
    keys_alive = redis.keys('product-*')
    products = [redis.get(k).decode('utf-8') for k in keys_alive]
    return jsonify({'products': products})


# @catalog.route('/product/<key>')
# def product(key):
#     product = Product.objects.get_or_404(key=key)
#     return 'Product - %s, $%s' % (product.name, product.price)


# @catalog.route('/products')
# def products():
#     products = Product.objects.all()
#     res = {}
#     for product in products:
#         res[product.key] = {
#             'name': product.name,
#             'price': str(product.price),
#         }
#     return jsonify(res)

# @catalog.route('/product-create', methods=['POST',])
# def create_product():
#     name = request.form.get('name')
#     key = request.form.get('key')
#     price = request.form.get('price')
#     product = Product(
#         name=name,
#         key=key,
#         price=Decimal(price)
#     )
#     product.save()
#     return 'Product created.'
