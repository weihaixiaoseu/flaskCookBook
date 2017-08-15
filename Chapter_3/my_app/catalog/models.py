import datetime
from my_app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return '<Product %d>' % self.id


# class Product(db.Document):
#     created_at = db.DateTimeField(
#         default=datetime.datetime.now, required=True
#     )
#     key = db.StringField(max_length=255, required=True)
#     name = db.StringField(max_length=255, required=True)
#     price = db.DecimalField()

#     def __repr__(self):
#         return '<Product %r>' % self.id
