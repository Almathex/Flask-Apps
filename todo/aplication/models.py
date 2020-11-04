from aplication import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable =False)
    complete = db.Column(db.Integer, nullable=False)

class Form(FlaskForm):
    task = StringField('First Name')
    submit = SubmitField('Add task')    
