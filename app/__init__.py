from flask import Flask
from flask.ext.bootstrap import Bootstrap
bs = Bootstrap()
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt()
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.login_view = '/'


def create_app(config):
    """
    Creates a flask app that does not initially bundle the extensions with it,
    which allows them to easily be used elsewhere.

    Args:
        config (object): The configuration object to use.

    Returns:
        app (object): The Python Flask object.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    bs.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.views import bp
    app.register_blueprint(bp)

    return app
