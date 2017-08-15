from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy 
from redis import Redis


app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {'DB': 'my_catalog'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.debug = True
# db = MongoEngine(app)
db = SQLAlchemy(app)


redis = Redis()

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()