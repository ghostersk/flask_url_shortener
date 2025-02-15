from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tiny0.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

# Initialize the database
from tiny0.models import URL
# DB needs to run in context, for Python 3.10 at least and newest packages
with app.app_context():    
    db.create_all()

from tiny0 import routes
