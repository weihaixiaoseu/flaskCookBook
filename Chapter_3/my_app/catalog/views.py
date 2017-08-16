from decimal import Decimal
from flask import request, Blueprint, jsonify
from my_app.catalog.models import Product
from my_app import db

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


@catalog.route('/product/<key>')
def product(key):
    product = Product.query.get_or_404(key)
    return 'Product - %s, $%s' % (product.name, product.price)


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
        }
    return jsonify(res)


@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(name, price)
    db.session.add(product)
    db.session.commit()
    return 'Product created.'



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
