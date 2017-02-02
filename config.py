import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    CURRENCY = "gbp"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ["PURCHASE_EMAIL"]
    MAIL_PASSWORD = os.environ["PURCHASE_PASSWORD"]
    STRIPE_SECRET = os.environ['STRIPE_SECRET']
    STRIPE_PUBLISHABLE = os.environ['STRIPE_PUBLISHABLE']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ErrorMessages:

    ITEM_SIZE = "Please select a size."

    ITEM_COLOUR = "Please select a colour."