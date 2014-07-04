from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, validators


class LoginForm(Form):
    username = StringField('Username: ', [validators.Required(message='You must provide a username.')])
    password = PasswordField('Password: ', [validators.Required(message='You must provide a password.')])
    submit = SubmitField('Log in')


class CreateForm(Form):
    forename = StringField('Forename: ', [validators.Required(message='A forename must be provided')])
    surname = StringField('Surname: ', [validators.Required(message='A surname must be provided.')])
    dob = StringField('D.O.B: ', [validators.Required(message='A date of birth must be provided.')])
    mobile = StringField('Mobile number: ', [validators.Required(message='A mobile number must be provided.')])
    submit = SubmitField('Submit')
