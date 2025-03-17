from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    """Flask App Factory"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['VT_API_KEY'] = os.getenv('VT_API_KEY')

    db.init_app(app)

    with app.app_context():
        from . import models  # Import models inside the context
        db.create_all()

    from .routes import main_bp  # Import and register blueprint
    app.register_blueprint(main_bp)

    return app
