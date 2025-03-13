from flask import Flask
# from flask_login import LoginManager
from .views.home import home_blueprint
from .views.login import login_blueprint
from .views.sphere2riches import sphere2riches_blueprint

# login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('config')    # Now we can access the global configuration variables via app.config["VAR_NAME"].
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
# app.config.from_pyfile('../instance/config.py')
# app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = True

from .util import assets
app.register_blueprint(home_blueprint, url_prefix='/')
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(sphere2riches_blueprint, url_prefix='/sphere2riches')

# TODO: SQLAlchemy - learn more & setup, is it even needed ??
# Update: Program works with msql.connector => What is the purpose of SQLAlchemy?
# db = SQLAlchemy(app)

app.secret_key = b'_asdasd\t5#y2L"F4Q8z\n\xec]/'
login_manager.init_app(app)
