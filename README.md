# ATC Cardiff

A web application to gather patient data at Cardiff's [Alchohol Treatment Centre](http://www.walesprobationtrust.gov.uk/alcohol-treatment-centre-2/) (ATC). The data harvested by this app will be used as a **plugin** to *personalise* the [SMS intervention service](https://github.com/jawrainey/sris).

## Requirements

This app was built using [Flask](https://github.com/mitsuhiko/flask) with several extensions to make life easier. These include:

- [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap): access to Twitter-Bootstrap assets.
- [FlaskSQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy): easy ORM access to databases in Python.
- [FlaskWTF](https://github.com/lepture/flask-wtf): secure form creation and access.

## Building locally

To install the dependendies I recommend creating a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):

    virtualenv atcenv
    source atcenv/bin/activate
    pip install -r requirements.txt

The site can be viewed [locally](http://localhost:5000) by running the flask app:

    python run.py

## Contributing

If you have any suggestions then please open an [issue](https://github.com/jawrainey/?/issues) or make a [pull request](https://github.com/jawrainey/atc-app/pulls).
