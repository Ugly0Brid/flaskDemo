from flask import Flask
from config import config
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .rsc import rsc as rsc_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(rsc_blueprint, url_prefix='/rsc')
    return app
