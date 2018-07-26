import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class InfoFilter(logging.Filter):
    def filter(self, record):
        """only use INFO
        筛选, 只需要 INFO 级别的log
        :param record:
        :return:
        """
        if logging.INFO <= record.levelno < logging.ERROR:
            # 已经是INFO级别了
            # 然后利用父类, 返回 1
            return super().filter(record)
        else:
            return 0


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or '0i@lri)9v81y**w!41(&0&8ol#14@d_6fu12-#5)1xatgu5b^8'
    SQLALCHEMY_COMMIT_ON_TEARDOWW = True
    LOG_PATH = os.path.join(basedir, "logs")
    LOG_PATH_ERROR = os.path.join(LOG_PATH, "error.log")
    LOG_PATH_INFO = os.path.join(LOG_PATH, "info.log")
    LOG_FILE_MAX_BYTES = 20 * 1024 * 1024
    LOG_FILE_BACK_COUNT = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zfj@123@127.0.0.1:13306/flaskOps?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging
        from logging.handlers import RotatingFileHandler
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(thread)d %(funcName)s %(pathname)s %(lineno)s %(message)s')
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR)
        file_handler_error.setFormatter(formatter)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)


config = {
    'default': DevelopmentConfig
}
