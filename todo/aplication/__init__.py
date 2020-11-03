from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password1234@35.197.211.81/todo"

db = SQLAlchemy(app)

from aplication import routes
