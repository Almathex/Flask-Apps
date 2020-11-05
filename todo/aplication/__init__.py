from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password1234@34.105.143.130/todo"

db = SQLAlchemy(app)

from aplication import routes
