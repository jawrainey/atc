# ATC Cardiff

A web application developed to gather patient data at Cardiff's [Alcohol Treatment Centre](http://www.walesprobationtrust.gov.uk/alcohol-treatment-centre-2/) (ATC). Data gathered by this application will be used to initiate conversation with the [SMS intervention service](https://github.com/jawrainey/sris).

**Note:** this and the [associated intervention service](https://github.com/jawrainey/sris) were developed as a means of exploring SMS as a means of intervention. Neither are in production use, and have been made open-source to promote the ideas explored, as well as the interface and techniques implemented.

# Screenshots

The login screen for ATC:

![Login screen](https://i.imgur.com/h4Piyf3.png?1 "Login screen")

The interface for adding new ATC patients:

![Adding user - note error found](https://i.imgur.com/9nd5O52.png?1 "Adding user - note error found")

The same interface having automatically cleared the field and displayed error message to user:

![Adding user - note error message](https://i.imgur.com/GKjRgne.png?1 "Adding user - note error message")

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

## Contributing

If you have any suggestions then please open an [issue](https://github.com/jawrainey/atc/issues) or make a [pull request](https://github.com/jawrainey/atc/pulls).
