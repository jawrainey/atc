from app import models
from flask.ext.wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import StringField, SubmitField, PasswordField, validators

import datetime
import re


class LoginForm(Form):
    username = StringField('Username: ', [validators.Required(
        message='You must provide a username.')])
    password = PasswordField('Password: ', [validators.Required(
        message='You must provide a password.')])
    submit = SubmitField('Log in')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        if not Form.validate(self):
            return False

        self.user = models.User.query.filter_by(
            username=self.username.data).first()

        if not self.user:
            self.username.errors.append('Unknown username provided.')

        if self.user and not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password provided.')

        if self.username.errors or self.password.errors:
            return False
        return True


class CreateForm(Form):
    forename = StringField('Forename: ', [validators.Required(
        message='A forename must be provided')])
    surname = StringField('Surname: ', [validators.Required(
        message='A surname must be provided.')])
    dob = StringField('D.O.B in format DD/MM/YYYY:', [validators.Required(
        message='A date of birth must be provided.')])
    mobile = StringField('Mobile number starting with 07 or 44: ',
                         [validators.Required(
                             message='A mobile number must be provided.')])
    submit = SubmitField('Submit')

    def validate(self):
        # Use the validators defined above first, e.g. empty fields.
        if not Form.validate(self):
            return False

        try:
            datetime.datetime.strptime(self.dob.data, "%d/%m/%Y")
        except ValueError:
            self.dob.errors.append("D.O.B format must be DD/MM/YYYY.")

        # Only accept valid UK mobile phone numbers
        # e,.g. in the format: 07111111111 or 447111111111
        rule = re.compile(r'^(07[\d]{8,12}|447[\d]{7,11})$')

        if not rule.search(self.mobile.data):
            self.mobile.errors.append("Invalid mobile number provided.")

        # Validate the UNIQUE mobile number against the DB.
        if models.Patient.query.get(self.mobile.data):
            self.mobile.errors.append(
                "A patient with that mobile number already exists.")

        # Show all errors generated above.
        if self.dob.errors or self.mobile.errors:
            return False
        else:
            return True

    def reset(self):
        self.process(MultiDict([]))
