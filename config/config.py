import os
from .config_reader import ConfigReader

basedir = os.path.abspath(os.path.dirname(__file__))

database_uri = None
try:
    reader = ConfigReader()
    db_config = reader.read_config(basedir + r'/config.json')
    database_uri = db_config.get_uri()
except Exception as e:
    print(e)


class Config:
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    NEWS_PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    if database_uri:
        SQLALCHEMY_DATABASE_URI = database_uri
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                                  'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    if database_uri:
        SQLALCHEMY_DATABASE_URI = database_uri
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                  'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
