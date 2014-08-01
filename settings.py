import os


class Config(object):
    """
    The shared configuration settings for the flask app.
    """
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "supersecretpassword"
    SECRET_KEY = 'supersecretpassword'


class ProdConfig(Config):
    """
    Setup the production configuration for the flask app.

    Args:
        Config (object): Inherit the default shared configuration settings.
    """
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://localhost/example')


class DevConfig(Config):
    """
    Setup the development configuration for the flask app.

    Args:
        Config (object): Inherit the default shared configuration settings.
    """
    ENV = 'dev'
    DEBUG = True
    DB_PATH = os.path.join(Config.PROJECT_ROOT, 'dev.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
