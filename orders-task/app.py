from flask import Flask
from

class Orders(db.Model):
    id = db.Colum(dc.Integer, primary_key=True)
    product_id - db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable = False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Orders', backref = 'product')

class Customers(db.Model):
    id + db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    orders = db.relationship('Orders', backref = 'customer')

if __name__=='__main__':
    app.run(debug=True)
