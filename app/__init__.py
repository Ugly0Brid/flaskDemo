import redis
from flask import Flask
from config import baseConfig
from celery import Celery
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

redis_store = FlaskRedis()
moment = Moment()
db = SQLAlchemy()
celery = Celery(__name__, broker=baseConfig["default"].CELERY_BROKER_URL)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(baseConfig[config_name])
    baseConfig[config_name].init_app(app)
    celery.conf.update(app.config)
    redis_store.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .rsc import rsc as rsc_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(rsc_blueprint, url_prefix='/rsc')
    return app
