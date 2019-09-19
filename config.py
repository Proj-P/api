import os


class Config(object):
    DEBUG = False
    # WTF_CSRF_ENABLED = False
    DATABASE_NAME = "projectp"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
    APP_STATIC = os.path.join(BASE_DIR, 'static')

    # Database (sqlite) configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = "aardappelpuree"


class ProductionConfig(Config):
    SECRET_KEY = "appeltaart"


config = {
    'development': DevelopmentConfig,
    'production': DevelopmentConfig
}
