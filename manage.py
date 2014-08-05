from flask.ext.script import Manager, Shell, prompt, prompt_pass
from app import create_app, models, db
from settings import DevConfig, ProdConfig
import os

if os.environ.get("ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)


@manager.command
def init_db():
    """
    Creates the database tables from SQLAlchemy models.

    Note: Opted to not use Flask-Migrate as it's quite heavyweight compared.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def create_user():
    """
    Creates a user in the database.
    """
    uname = prompt('Please enter a username')
    pword = prompt_pass('Please enter a password')
    db.session.add(models.User(username=uname, password=pword))
    db.session.commit()


def _context():
    """
    Expose shell session access to the app and db modules.

    Returns:
        dict: Exposing access to 'app' and 'db'.
    """
    return {'app': app, 'db': db}

manager.add_command('shell', Shell(make_context=_context))

if __name__ == '__main__':
    manager.run()
