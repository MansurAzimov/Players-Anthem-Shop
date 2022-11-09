from shop import db


class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer(),primary_key=True)
    title = 
    price
    category
    size
    description
    image