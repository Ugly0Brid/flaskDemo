import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or '0i@lri)9v81y**w!41(&0&8ol#14@d_6fu12-#5)1xatgu5b^8'
    SQLALCHEMY_COMMIT_ON_TEARDOWW = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@server:port/db'


config = {
    'default': DevelopmentConfig
}
