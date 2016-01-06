from datetime import timedelta


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'
    APP_NAME = '{} Server'
    SECRET_KEY = '{}'
    JWT_EXPIRATION_DELTA = timedelta(days=30)
    JWT_AUTH_URL_RULE = '/api/v1/auth'
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = '{}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    APP_NAME = '{} Production Server'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SUPPRESS_SEND = False


class TestingConfig(Config):
    TESTING = True
