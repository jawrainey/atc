# ATC Cardiff

A web application developed to gather patient data at Cardiff's [Alcohol Treatment Centre](http://www.walesprobationtrust.gov.uk/alcohol-treatment-centre-2/) (ATC). Data gathered by this application will be used to initiate conversation with the [SMS intervention service](https://github.com/jawrainey/sris).

## Deployment

### Database creation

To create the database tables invoke the `init_db` method:

    python manage.py init_db

### Adding users

As there is no means of registration, a user (or additional users) needs to be created manually. This can be achieved by invoking the `create_user` method:

    python manage.py create_user

### Environment variables

#### Database access

To enable `postgresql` access, the [database](https://github.com/jawrainey/atc/blob/master/settings.py#L23) environment variable `DATABASE_URL` needs to be set to the string of your `postgresql` of your database.

#### Production configuration

The [configuration variable](https://github.com/jawrainey/atc/blob/master/manage.py#L6) `ENV` needs to be set to `prod` to disable debugging and enable `postgresql` database access.

## Building locally

### Installing dependencies

I recommend creating a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) when developing:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Viewing the site

The site can be viewed locally by running the flask app:

    python manage.py runserver

### Shell access

For shell access to the `app` and `db` variables, pass the `shell` parameter to `manage.py`:

    python manage.py shell

## License

- Licensed under [MIT](https://github.com/jawrainey/atc/blob/master/LICENSE.txt).

**Note:** this application was developed as experiment to facilitate the associated intervention service. This, nor the intervention service are currently being used, and is being made open-source to promote the idea of SMS for interventions.

## Contributing

If you have any suggestions then please open an [issue](https://github.com/jawrainey/atc/issues) or make a [pull request](https://github.com/jawrainey/atc/pulls).
