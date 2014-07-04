import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

DEBUG = True

CSRF_ENABLED = True
CSRF_SESSION_KEY = "supersecretpassword"
SECRET_KEY = 'supersecretpassword'
