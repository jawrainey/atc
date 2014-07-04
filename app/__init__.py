from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app import views, models
