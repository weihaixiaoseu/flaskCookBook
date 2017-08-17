from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy 
from redis import Redis
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
# import os

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {'DB': 'my_catalog'}
 
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.debug = True
# db = MongoEngine(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand) 

redis = Redis()

from my_app.catalog.views import catalog
app.register_blueprint(catalog)



