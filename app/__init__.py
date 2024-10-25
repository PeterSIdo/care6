# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.db_connection.conn import init_db_connection
from app.login.auth import auth_bp
from app.data_input.input import input_bp
from app.data_output.output import output_bp
from app.admin.admin import admin_bp
from app.main.main import main_bp
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load configurations from the Config class
    app.config.from_object(Config)

    # Explicitly set SQLALCHEMY_DATABASE_URI using the get_db_uri method from Config
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_db_uri()

    # Initialize the database connection
    db.init_app(app)
    init_db_connection(app)

    # Register Blueprints
    from app.routes import routes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(input_bp)
    app.register_blueprint(output_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(routes_bp)

    return app