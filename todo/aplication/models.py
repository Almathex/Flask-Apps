from aplication import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(30))
    status = db.Column(db.String(30), nullable = False)
    
