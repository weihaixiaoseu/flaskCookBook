from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')

app = Flask(__name__) 
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.debug = True 
db = SQLAlchemy(app) 




class Product(db.Model):
	__tablename__='product'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	category = db.relationship('Category', backref=db.backref('product',lazy='dynamic'),lazy='joined')

	def __repr__(self):
		return '<Product %s>' %self.name 

class Category(db.Model):
	__tablename__='category'
	id = db.Column(db.Integer, primary_key=True)
	categoryName = db.Column(db.String(32))
	# product = db.relationship('Product', backref='category')

	def __repr__(self):
		return '<Category %s>' %self.categoryName
