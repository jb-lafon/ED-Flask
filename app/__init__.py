# ==========
# File : __init__.py.py
# Author : Jb
# First created on : 21/11/2018
# Description: App init file
# ==========

# third-party imports
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# local imports
from config import app_config
from os import getenv

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

appli = Flask(__name__, instance_relative_config=True)


def create_app(app, config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    from app import models
    # from .DB_upload import upload_json
    from .alchemydb.systems_db import value_search

    from .views import home_blueprint, upload_blueprint, value_search_blueprint, s2r_blueprint, w2r_blueprint
    from .util import assets
    app.register_blueprint(home_blueprint, url_prefix='/')
    app.register_blueprint(upload_blueprint, url_prefix='/upload')
    # app.register_blueprint(upload_7days_blueprint, url_prefix='/upload7days')
    app.register_blueprint(value_search_blueprint, url_prefix='/value-search')
    app.register_blueprint(s2r_blueprint, url_prefix='/s2r')
    app.register_blueprint(w2r_blueprint, url_prefix='/w2r')

    return app


config_slug = getenv('FLASK_CONFIG')
app = create_app(appli, config_slug)
