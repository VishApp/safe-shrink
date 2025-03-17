from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['VT_API_KEY'] = os.getenv('VT_API_KEY')  # Optional VirusTotal API Key

db = SQLAlchemy(app)

from . import routes, models

with app.app_context():
    db.create_all()
