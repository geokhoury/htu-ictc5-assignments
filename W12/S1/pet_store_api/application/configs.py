import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    # Flask config
    SECRET_KEY = '^753*&FdFS#4D'

    # MONGOALCHEMY_SERVER='localhost'
    MONGOALCHEMY_USER = 'root'
    MONGOALCHEMY_PASSWORD = 'example'
    MONGOALCHEMY_DATABASE = 'flaskdo'
    MONGOALCHEMY_SERVER_AUTH = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.sqlite')  # NOQA


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.sqlite')  # NOQA


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
