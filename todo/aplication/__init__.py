from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password1234@35.234.134.185/todo"

db = SQLAlchemy(app)

from aplication import routes
