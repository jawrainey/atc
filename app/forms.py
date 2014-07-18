from app import models
from flask.ext.wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import TextField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Required
import datetime
import re


class LoginForm(Form):
    username = TextField('Username: ', [DataRequired(
        message='You must provide a username.'),
        Length(min=3, max=25)])
    password = PasswordField('Password', [DataRequired(
        message='You must provide a password.'),
        Length(min=4, max=40)])
    submit = SubmitField('Log in')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        # Use the validators defined above first, e.g. empty fields.
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
    forename = StringField('Forename: ', [Required(
        message='A forename must be provided')])
    surname = StringField('Surname: ', [Required(
        message='A surname must be provided.')])
    dob = StringField('D.O.B:', [Required(
        message='A date of birth must be provided.')])
    mobile = StringField('Mobile number: ',
                         [Required(
                             message='A mobile number must be provided.')])
    submit = SubmitField('Submit')

    def validate(self):
        if not Form.validate(self):
            return False

        try:
            datetime.datetime.strptime(self.dob.data, "%d/%m/%Y")
        except ValueError:
            self.dob.errors.append("D.O.B format must be DD/MM/YYYY.")

        # Only accept valid UK mobile phone numbers in international format.
        rule = re.compile(r'^(447[\d]{7,11})$')

        if not rule.search(self.mobile.data):
            self.mobile.errors.append("Invalid mobile number provided.")

        # Validate the UNIQUE mobile number against the DB.
        if models.Patient.query.get(self.mobile.data):
            self.mobile.errors.append(
                "A patient with that mobile number already exists.")

        if self.dob.errors or self.mobile.errors:
            return False
        return True

    def reset(self):
        self.process(MultiDict([]))
