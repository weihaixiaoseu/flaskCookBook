from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy 
from redis import Redis
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 




app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {'DB': 'my_catalog'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.debug = True
# db = MongoEngine(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand) 

redis = Redis(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)



