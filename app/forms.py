from app import models
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, validators

import datetime
import re

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

    def validate(self):
        # Use the validators defined above first, e.g. empty fields.
        if not Form.validate(self):
            return False

        # Validate the date of birth against
        try:
            datetime.datetime.strptime(self.dob.data, "%d/%m/%Y")
        except ValueError:
            self.dob.errors.append("D.O.B format must be DD/MM/YYYY.")

        # Only accept valid UK mobile phone numbers in the format: 07111111111 or 447111111111
        rule = re.compile(r'^\+?(44)?(0|7)\d{9,13}$')

        if not rule.search(self.mobile.data):
            self.mobile.errors.append("Invalid mobile number provided.")

        # Validate the UNIQUE mobile number against the DB.
        if models.Patient.query.get(self.mobile.data):
            self.mobile.errors.append("A patient with that mobile number already exists.")

        # Show all errors generated above.
        if self.dob.errors or self.mobile.errors:
            return False
        else:
            # All is well on the validation front.
            return True
